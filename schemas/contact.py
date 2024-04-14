from pydantic import BaseModel, Field, EmailStr, HttpUrl
from datetime import datetime

class Contact(BaseModel):# 継承
    id:int
    name: str = Field(..., min_length=2, max_length=50)# ...は必須
    email: EmailStr
    url: HttpUrl | None = Field(default=None) 
    gender: int = Field(..., strict=True, ge=0, le=2) # strictは厳密な値を指定, geはgreater than or equal to, leはless than or equal to
    message: str = Field(..., max_length=200)
    is_enabled: bool = Field(default=False)
    created_at: datetime