from sqlalchemy import Column, Integer, String, Boolean, DateTime
from database import Base
from datetime import datetime


class Contact(Base): # 継承
    __tablename__ = "contacts" # テーブル名
    id = Column(Integer, primary_key=True, autoincrement=True) # 主キー、自動インクリメント
    name = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False)
    url = Column(String(255), nullable=True)
    gender = Column(Integer, nullable=False) # enumで設定するパターンもある
    message = Column(String(200), nullable=False)
    is_enabled = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now()) 