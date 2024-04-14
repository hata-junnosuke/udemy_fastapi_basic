from pydantic import BaseModel, Field, EmailStr, HttpUrl
from datetime import datetime

# 一覧表示用モデル
class ContactList(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    created_at: datetime
    class Config:
        from_attributes = True

# ベースモデル
class ContactBase(BaseModel):# 継承
    name: str = Field(..., min_length=2, max_length=50)# ...は必須
    email: EmailStr
    url: HttpUrl | None = Field(default=None) 
    gender: int = Field(..., strict=True, ge=0, le=2) # strictは厳密な値を指定, geはgreater than or equal to, leはless than or equal to
    message: str = Field(..., max_length=200)
    is_enabled: bool = Field(default=False)
    class Config:
        from_attributes = True

# 詳細表示用モデル
class ContactDetail(ContactBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

# 登録用モデル
class ContactCreate(ContactBase):
    pass