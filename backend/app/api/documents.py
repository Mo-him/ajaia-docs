from html import escape
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.document import Document, DocumentShare
from app.models.user import User
from app.repositories.documents import visible_documents
from app.services.documents import require_read, require_edit, share_document
from app.schemas.document import DocumentCreate, DocumentUpdate, DocumentResponse, ShareCreate, ShareResponse

router = APIRouter(prefix="/documents", tags=["documents"])
MAX_FILE_SIZE = 2 * 1024 * 1024


def response(doc: Document, access: str):
    return DocumentResponse(id=doc.id, title=doc.title, content=doc.content, owner_id=doc.owner_id, owner_name=doc.owner.name, updated_at=doc.updated_at, access=access)

@router.get("", response_model=list[DocumentResponse])
def list_documents(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    docs = visible_documents(db, user.id)
    return [response(d, "owner" if d.owner_id == user.id else "shared") for d in docs]

@router.post("", response_model=DocumentResponse)
def create_document(data: DocumentCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    title = data.title.strip()
    if not title:
        raise HTTPException(422, "Title is required")
    doc = Document(title=title, content=data.content, owner_id=user.id)
    db.add(doc); db.commit(); db.refresh(doc)
    return response(doc, "owner")

@router.get("/{document_id}", response_model=DocumentResponse)
def get_document(document_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    doc = db.get(Document, document_id)
    require_read(doc, user.id)
    return response(doc, "owner" if doc.owner_id == user.id else "shared")

@router.put("/{document_id}", response_model=DocumentResponse)
def update_document(document_id: int, data: DocumentUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    doc = db.get(Document, document_id)
    require_edit(doc, user.id)
    title = data.title.strip()
    if not title:
        raise HTTPException(422, "Title is required")
    doc.title = title; doc.content = data.content
    db.commit(); db.refresh(doc)
    return response(doc, "owner" if doc.owner_id == user.id else "shared")

@router.delete("/{document_id}")
def delete_document(document_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    doc = db.get(Document, document_id)
    if not doc or doc.owner_id != user.id:
        raise HTTPException(404, "Document not found")
    db.delete(doc); db.commit()
    return {"message": "Document deleted"}

@router.post("/{document_id}/share", response_model=ShareResponse)
def share(document_id: int, data: ShareCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    doc = db.get(Document, document_id)
    if not doc: raise HTTPException(404, "Document not found")
    share = share_document(db, doc, user.id, data.email)
    db.refresh(share)
    return ShareResponse(user_id=share.user_id, name=share.user.name, email=share.user.email, permission=share.permission)

@router.get("/{document_id}/shares", response_model=list[ShareResponse])
def shares(document_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    doc = db.get(Document, document_id)
    if not doc or doc.owner_id != user.id: raise HTTPException(403, "Only the owner can view sharing settings")
    return [ShareResponse(user_id=s.user_id, name=s.user.name, email=s.user.email, permission=s.permission) for s in doc.shares]

@router.post("/import", response_model=DocumentResponse)
async def import_file(file: UploadFile = File(...), db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    name = file.filename or ""
    if not name.lower().endswith((".txt", ".md")):
        raise HTTPException(400, "Only .txt and .md files are supported")
    raw = await file.read(MAX_FILE_SIZE + 1)
    if len(raw) > MAX_FILE_SIZE:
        raise HTTPException(400, "File is too large. Maximum size is 2 MB")
    text = raw.decode("utf-8", errors="replace")
    title = name.rsplit("/", 1)[-1].rsplit("\\", 1)[-1]
    if title.lower().endswith((".txt", ".md")):
        title = title.rsplit(".", 1)[0]
    # Preserve plain text safely inside HTML editor content.
    content = "<p>" + "</p><p>".join(escape(line) if line else "<br>" for line in text.splitlines()) + "</p>"
    doc = Document(title=title[:200] or "Imported document", content=content, owner_id=user.id)
    db.add(doc); db.commit(); db.refresh(doc)
    return response(doc, "owner")
