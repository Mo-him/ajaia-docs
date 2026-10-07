from datetime import datetime
from pydantic import BaseModel, Field

class DocumentCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    content: str = ""
class DocumentUpdate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    content: str
class ShareCreate(BaseModel):
    email: str
class ShareResponse(BaseModel):
    user_id: int
    name: str
    email: str
    permission: str
    model_config = {"from_attributes": True}
class DocumentResponse(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int
    owner_name: str
    updated_at: datetime
    access: str
