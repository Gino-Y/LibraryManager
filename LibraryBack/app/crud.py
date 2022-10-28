from sqlalchemy.orm import Session
from typing import List
import schemas
from app.models.models import Writer, Book, Publisher, Match


# from app.models import models
# user_info = db.query(models.Writer).filter(models.Writer.username == username).first()


def get_writer_by_username(db: Session, username: str):
    user_info = db.query(Writer).filter(Writer.username == username).first()
    return user_info


# 创建一个作者
def create_writer(db: Session, writer: schemas.WriterCreate):
    db_writer = Writer(**writer.dict())
    db.add(db_writer)
    db.commit()
    db.refresh(db_writer)
    return db_writer


# 获取所有作者信息
def get_all_writer(db: Session):
    return db.query(Writer).all()


def get_publisher_by_name(db: Session, name: str):
    publisher_info = db.query(Publisher).filter(Publisher.name == name).first()
    return publisher_info


# 创建一个出版社信息
def create_publisher(db: Session, publisher: schemas.PublisherCreate):
    db_publisher = Publisher(**publisher.dict())
    db.add(db_publisher)
    db.commit()
    db.refresh(db_publisher)
    return db_publisher


# 获取所有出版社信息
def get_all_publisher(db: Session):
    res = db.query(Publisher).all()
    return res


def get_book_by_title(db: Session, title: str):
    res = db.query(Book).filter(Book.title == title).first()
    return res


# 根据作者ID、出版社ID列表、书籍信息，创建书籍
def create_book_by_writer(db: Session, book: schemas.BookBase, writer_id: int, publisher_id_list: List[int]):
    db_book = Book(**book.dict(), writer_id=writer_id)
    publisher_obj_list = [db.query(Publisher).filter(Publisher.id == i).first() for i in publisher_id_list]
    db_book.book_to_publisher = publisher_obj_list
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    obj = {
        'id': db_book.id,
        'title': db_book.title,
        'price': db_book.price,
        'writer_id': db_book.writer_id,
        'publisher_data': db_book.publisher_data,
        'writers': db_book.book_to_writer,
        'publishers': db_book.book_to_publisher
        }
    return obj


# 获取所有的书籍信息
def get_all_books(db: Session):
    books = db.query(Book).all()
    result = list()
    for obj in books:
        parms = {
            'id': obj.id,
            'title': obj.title,
            'price': obj.price,
            'publisher_data': obj.publisher_data,
            'writers': obj.book_to_writer,
            'publishers': obj.book_to_publisher
        }
        result.append(parms)
    return result
