from sqlalchemy import Column, Integer, String, Float, ForeignKey, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)


class Invoice(Base):
    __tablename__ = 'invoices'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    status = Column(String, default='pending')
    amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    customer = relationship('Customer')


class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, ForeignKey('invoices.id'))
    amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    invoice = relationship('Invoice')


class Configuration(Base):
    __tablename__ = 'configurations'
    id = Column(Integer, primary_key=True)
    instance_type = Column(String, nullable=False)
    conditions = Column(JSON, nullable=False)  # To store dynamic conditions (as JSON)
    actions = Column(JSON, nullable=False)  # To store actions (as JSON)
