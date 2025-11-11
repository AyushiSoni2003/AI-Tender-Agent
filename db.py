# db.py
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Tender(Base):
    __tablename__ = 'tenders'
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    description = Column(Text)
    requirements = Column(Text)
    budget = Column(String(100))
    deadline = Column(String(100))

engine = create_engine("sqlite:///tenders.db")
Session = sessionmaker(bind=engine)
session = Session()

def get_tender_data(tender_id):
    return session.query(Tender).filter(Tender.id == tender_id).first()

def get_all_tenders():
    return session.query(Tender).all()