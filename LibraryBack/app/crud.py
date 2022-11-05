"""
ORM操作数据库动作
"""
from sqlalchemy.orm import Session
from typing import List
import schemas
from app.models.models import Writer, Book, Publisher, Match


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


def writer_delete(db: Session, id: schemas.WriterDelete):
    id = int(id)
    # 先删除match的数据
    # match_info = db.query(Match).filter(Match.writer_id == id).delete()
    # db.commit()
    writer_info = db.query(Writer).filter(Writer.id == id).delete()
    db.commit()


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


def publisher_delete(db: Session, id: schemas.PublisherDelete):
    id = int(id)
    # 先删除match的数据
    match_info = db.query(Match).filter(Match.publisher_id == id).delete()
    db.commit()
    publisher_info = db.query(Publisher).filter(Publisher.id == id).delete()
    db.commit()


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


def book_update(db: Session, book: schemas.BookCreate):
    # 根据id查询数据信息，然后修改信息
    book_info = db.query(Book).filter(Book.id == book.id).first()
    book_info.id = book.id
    book_info.title = book.title
    book_info.price = book.price
    book_info.writer_id = book.writer_id
    db.commit()
    # 先删除match的数据
    match_info = db.query(Match).filter(Match.book_id == book.id).delete()
    db.commit()
    # 重新写入match数据
    publishers = book.publishers
    for publisher in publishers:
        match = Match()
        match.book_id = book.id
        match.publisher_id = publisher
        db.add(match)
        db.commit()


def publisher_update(db: Session, publisher: schemas.Publisher):
    # 根据id查询数据信息，然后修改信息
    publisher_info = db.query(Publisher).filter(Publisher.id == publisher.id).first()
    publisher_info.id = publisher.id
    publisher_info.name = publisher.name
    db.commit()
    # 先删除match的数据
    match_info = db.query(Match).filter(Match.publisher_id == publisher.id).delete()
    db.commit()
    # 重新写入match数据
    publishers = publisher.publishers
    for publisher in publishers:
        match = Match()
        match.book_id = publisher.id
        match.publisher_id = publisher
        db.add(match)
        db.commit()


def book_delete(db: Session, id: schemas.BookDelete):
    id = int(id)
    # 先删除match的数据
    match_info = db.query(Match).filter(Match.book_id == id).delete()
    db.commit()
    book_info = db.query(Book).filter(Book.id == id).delete()
    db.commit()


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
