from sqlalchemy import select
from app.core.database import Base, engine, SessionLocal
from app.core.security import hash_password
from app.models.user import User
from app.models.document import Document

Base.metadata.create_all(bind=engine)
db = SessionLocal()
try:
    users = [
        ("Mohim", "mohim@ajaia.dev"),
        ("Jane", "jane@ajaia.dev"),
    ]
    for name, email in users:
        if not db.scalar(select(User).where(User.email == email)):
            db.add(User(name=name, email=email, password_hash=hash_password("Demo@123")))
    db.commit()
    print("Seed complete. Both demo users use password Demo@123")
finally:
    db.close()
