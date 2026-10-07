import os

os.environ["DATABASE_URL"] = "sqlite:///./test_ajaia.db"
os.environ["JWT_SECRET"] = "test-secret"

from fastapi.testclient import TestClient

from app.main import app
from app.core.database import Base, engine, SessionLocal
from app.core.security import hash_password
from app.models.user import User
from app.models.document import Document, DocumentShare


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


db = SessionLocal()

for name, email in [
    ("Owner", "owner@test.dev"),
    ("Shared", "shared@test.dev"),
    ("Other", "other@test.dev"),
]:
    db.add(
        User(
            name=name,
            email=email,
            password_hash=hash_password("Password1!"),
        )
    )

db.commit()
db.close()

client = TestClient(app)


def token(email):
    r = client.post(
        "/api/auth/login",
        json={
            "email": email,
            "password": "Password1!",
        },
    )

    assert r.status_code == 200

    return r.json()["access_token"]


def test_shared_user_can_read_but_other_cannot():
    owner = token("owner@test.dev")
    shared = token("shared@test.dev")
    other = token("other@test.dev")

    r = client.post(
        "/api/documents",
        headers={
            "Authorization": f"Bearer {owner}"
        },
        json={
            "title": "Shared Doc",
            "content": "<p>Hello</p>",
        },
    )

    assert r.status_code == 200

    doc_id = r.json()["id"]

    r = client.post(
        f"/api/documents/{doc_id}/share",
        headers={
            "Authorization": f"Bearer {owner}"
        },
        json={
            "email": "shared@test.dev"
        },
    )

    assert r.status_code == 200

    assert (
        client.get(
            f"/api/documents/{doc_id}",
            headers={
                "Authorization": f"Bearer {shared}"
            },
        ).status_code
        == 200
    )

    assert (
        client.get(
            f"/api/documents/{doc_id}",
            headers={
                "Authorization": f"Bearer {other}"
            },
        ).status_code
        == 404
    )