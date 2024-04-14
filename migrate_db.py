from sqlalchemy.ext.asyncio import create_async_engine
from models.contact import Base
import asyncio

DB_URL = "sqlite+aiosqlite:///fastapi-app.db"
engine = create_async_engine(DB_URL, echo=True)

async def reset_database():
    async with engine.begin() as conn: # with 例外発生時でもリソース解放される
        await conn.run_sync(Base.metadata.drop_all) # テーブル削除
        await conn.run_sync(Base.metadata.create_all) # テーブル作成
    
if __name__ == "__main__": # スクリプトで実行時のみ実行
    asyncio.run(reset_database())