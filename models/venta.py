from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Venta(Base):
    __tablename__ = 'ventas'
    id = Column(Integer, primary_key=True, index=True)
    producto = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    comprador_email = Column(String, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)
