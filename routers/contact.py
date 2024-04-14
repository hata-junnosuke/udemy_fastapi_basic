from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import schemas.contact as contact_schema
import cruds.contact as contact_crud
from database import get_db
from datetime import datetime

router = APIRouter()

@router.get("/contacts", response_model=list[contact_schema.ContactList])
async def get_contact_all(db: AsyncSession = Depends(get_db)):
    return await contact_crud.get_contact_all(db)
    # dummy_date = datetime.now()
    # return [contact_schema.Contact(
    #     id=1, 
    #     name="山田", 
    #     email="test@test.com", 
    #     url="http://test.com",
    #     gender=1, 
    #     message="テスト", 
    #     is_enabled=False, 
    #     created_at=dummy_date
    #     )]

@router.post("/contacts", response_model=contact_schema.ContactCreate)
async def create_contact(body: contact_schema.ContactCreate, db: AsyncSession = Depends(get_db)):
    return await contact_crud.create_contact(db, body)
    # return contact_schema.Contact(**body.model_dump())# model_dump()は辞書型に変換, **は辞書型を引数に展開

@router.get("/contacts/{id}", response_model=contact_schema.ContactDetail)
async def get_contact(id: int, db: AsyncSession = Depends(get_db)):
    contact = await contact_crud.get_contact(db, id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@router.put("/contacts/{id}", response_model=contact_schema.ContactCreate)
async def update_contact(id: int, body: contact_schema.ContactCreate, db: AsyncSession = Depends(get_db)):
    contact = await contact_crud.get_contact(db, id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return await contact_crud.update_contact(db, body, original=contact)

@router.delete("/contacts/{id}", response_model=None)
async def delete_contact(id: int, db: AsyncSession = Depends(get_db)):
    contact = await contact_crud.get_contact(db, id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return await contact_crud.delete_contact(db, original=contact)

def get_message():
    message = "Hello, World!"
    print(f"get_messageが実行された: {message}")
    return message

@router.get("/depends")
async def main(message: str = Depends(get_message)):
    print(f"エンドポイントにアクセスがあった: {message}")
    return {"message": message}