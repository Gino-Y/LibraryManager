
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime

from app.database import Base


class Writer(Base):
    __tablename__ = 'writer'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(32), index=True)
    email = Column(String(32))
    writer_to_book = relationship('Book', backref='book_to_writer')


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(32))
    price = Column(Float)
    publisher_data = Column(DateTime, default=datetime.datetime.now)
    writer_id = Column(Integer, ForeignKey('writer.id'))


class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32))
    publisher_to_book = relationship('Book', backref='book_to_publisher', secondary='match')


class Match(Base):
    __tablename__ = 'match'
    id = Column(Integer, primary_key=True, index=True)
    publisher_id = Column(Integer, ForeignKey('publisher.id'))
    book_id = Column(Integer, ForeignKey('book.id'))
