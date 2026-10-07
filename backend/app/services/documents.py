from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.document import Document, DocumentShare
from app.models.user import User


def can_read(doc: Document, user_id: int) -> bool:
    return doc.owner_id == user_id or any(s.user_id == user_id for s in doc.shares)

def can_edit(doc: Document, user_id: int) -> bool:
    return doc.owner_id == user_id or any(s.user_id == user_id and s.permission == "editor" for s in doc.shares)

def require_read(doc: Document | None, user_id: int):
    if not doc or not can_read(doc, user_id):
        raise HTTPException(404, "Document not found")

def require_edit(doc: Document | None, user_id: int):
    if not doc or not can_edit(doc, user_id):
        raise HTTPException(403, "You do not have edit access to this document")

def share_document(db: Session, doc: Document, owner_id: int, email: str):
    if doc.owner_id != owner_id:
        raise HTTPException(403, "Only the owner can share this document")
    target = db.scalar(select(User).where(User.email == email.lower().strip()))
    if not target:
        raise HTTPException(404, "User not found")
    if target.id == owner_id:
        raise HTTPException(400, "Owner already has access")
    existing = db.scalar(select(DocumentShare).where(DocumentShare.document_id == doc.id, DocumentShare.user_id == target.id))
    if existing:
        return existing
    share = DocumentShare(document_id=doc.id, user_id=target.id, permission="editor")
    db.add(share)
    db.commit()
    db.refresh(share)
    return share
