from sqlalchemy import select, or_
from sqlalchemy.orm import Session
from app.models.document import Document, DocumentShare


def visible_documents(db: Session, user_id: int):
    return db.scalars(select(Document).outerjoin(DocumentShare, DocumentShare.document_id == Document.id).where(or_(Document.owner_id == user_id, DocumentShare.user_id == user_id)).order_by(Document.updated_at.desc())).unique().all()


def get_document(db: Session, document_id: int):
    return db.get(Document, document_id)
