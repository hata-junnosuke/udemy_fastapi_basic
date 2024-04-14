from typing import List, Tuple
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
import schemas.contact as contact_schema
import models.contact as contact_model
from datetime import datetime

async def create_contact(db: AsyncSession, contact: contact_schema.ContactCreate) -> contact_model.Contact:
    """
    DBに新規保存
    引数:
        db: DBセッション
        contact: 作成するコンタクトのデータ
    戻り値:
        作成されたORMモデル
    """
    contact_data = contact.model_dump()
    if contact_data["url"] is not None:
        contact_data["url"] = str(contact_data["url"])

    db_contact = contact_model.Contact(**contact_data) # db保存はsqlalchemyのモデルを使う。インスタンス化

    db.add(db_contact) # セッションに追加
    await db.commit() # コミット
    await db.refresh(db_contact) # DBから最新の情報を取得
    return db_contact

async def get_contact_all(db: AsyncSession) -> List[Tuple[int, str, datetime]]:
    """
    DBから全件取得
    引数:
        db: DBセッション
    戻り値:
        取得したデータ
    """
    result: Result = await db.execute(
        select(
            contact_model.Contact.id,
            contact_model.Contact.name,
            contact_model.Contact.created_at
        )
    )
    return result.all()

async def get_contact(db: AsyncSession, id: int) -> contact_model.Contact | None:
    """
    DBからIDで取得
    引数:
        db: DBセッション
        id: 取得するID
    戻り値:
        取得したデータ
    """
    query = select(contact_model.Contact).where(contact_model.Contact.id == id)
    result: Result = await db.execute(query)
    return result.scalars().first() # scalars()は1つの値を取得, first()は最初の値を取得

async def update_contact(db: AsyncSession, contact: contact_schema.ContactCreate, original: contact_model.Contact) -> contact_model.Contact:
    """
    DBを更新
    引数:
        db: DBセッション
        contact: 更新するデータ
        original: 更新前のデータ
    戻り値:
        更新されたORMモデル
    """
    original.name = contact.name
    original.email = contact.email
    if original.url is not None:
        original.url = str(contact.url)
    original.gender = contact.gender
    original.message = contact.message
    db.add(original) # セッションに追加
    await db.commit() # コミット
    await db.refresh(original) # DBから最新の情報を取得
    return original

async def delete_contact(db: AsyncSession, original: contact_model.Contact) -> None:
    await db.delete(original)
    await db.commit()
    