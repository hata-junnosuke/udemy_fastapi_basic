from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "sqlite+aiosqlite:///fastapi-app.db" # SQLiteの非同期対応
engine = create_async_engine(DB_URL, echo=True)

Base = declarative_base()
# DBセッションオブジェクトを生成
db_session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession)
async def get_db():
    async with db_session() as session:
        yield session