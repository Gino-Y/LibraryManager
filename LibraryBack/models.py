from database import Base
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime


class Writer(Base):
    __tablename__ = 'writer'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(32), index=True)
    email = Column(String(32))
    writer_to_book = relationship('book', backref='book_to_writer')


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(32))
    price = Column(Float)
    publish_data = Column(DateTime, default=datetime.datetime.now)
    author_id = Column(Integer, ForeignKey('writer.id'))


class Publish(Base):
    __tablename__ = 'publish'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32))
    publish_to_book = relationship('book', backref='book_to_publish', secondary='match')


class Match(Base):
    __tablename__ = 'match'
    id = Column(Integer, primary_key=True, index=True)
    publish_id = Column(Integer, ForeignKey('publish.id'))
    book_id = Column(Integer, ForeignKey('book.id'))
