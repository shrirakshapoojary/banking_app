from sqlalchemy import Column, Integer, String
from .database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    balance = Column(Integer, default=0)


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer)
    amount = Column(Integer)
    type = Column(String(20))  # deposit / withdraw