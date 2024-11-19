from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class CompanyModel(Base):
    __tablename__ = 'nepse'
    symbol = Column(String, primary_key=True)
    close_price = Column(Float)
    open_price = Column(Float)
    high_price = Column(Float)
    low_price = Column(Float)
    total_traded_quantity = Column(Integer)
    total_traded_value = Column(Float)
    total_trades = Column(Integer)
    ltp = Column(Float)
    previous_day_close_price = Column(Float)
    average_traded_price = Column(Float)
    fifty_two_week_high = Column('52_week_high', Float)
    fifty_two_week_low = Column('52_week_low', Float)
    marketcapitalization = Column(Float)
    date = Column(String, primary_key=True)

class Stock(BaseModel):
    symbol: str
    close_price: float
    open_price: float
    high_price: float
    low_price: float
    total_traded_quantity: float
    total_traded_value: float
    total_trades: int
    ltp: float
    previous_day_close_price: float
    average_traded_price: float
    fifty_two_week_high: float
    fifty_two_week_low: float
    marketcapitalization: float
    date: str

class StockResponse(BaseModel):
    companies: list[Stock]