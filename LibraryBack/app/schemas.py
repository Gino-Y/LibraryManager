"""
数据校验
"""
from datetime import datetime

from pydantic import BaseModel, EmailStr
from typing import Optional, List, Union


class WriterBase(BaseModel):
    username: str


class publisherBookUpdate(BaseModel):
    id: int
    title: str
    price: int
    writer_id: int
    publishers: list


class BookDelete(BaseModel):
    id: int


class PublisherDelete(BaseModel):
    id: int


class WriterDelete(BaseModel):
    id: int


# 作者请求体校验
class WriterCreate(WriterBase):
    email: EmailStr


# 作者响应体校验
class Writer(WriterBase):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


class PublisherBase(BaseModel):
    name: str


# 出版社请求体校验
class PublisherCreate(PublisherBase):
    pass


# 出版社响应体校验，这里也满足
class Publisher(PublisherBase):
    id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    price: float
    publisher_data: Optional[datetime] = None


# 书籍请求体校验模型
class BookCreate(BaseModel):
    writer_id: int
    publisher_id_list: List[int]
    book: BookBase


# 书籍响应体校验模型
class Book(BookBase):
    writer_id: int

    class Config:
        orm_mode = True


class BookAll(BaseModel):
    id: int
    title: str
    price: float
    publisher_data: datetime
    writers: Writer
    publishers: List[Publisher]


# 曾_成功
class GeneralDefine(BaseModel):
    message: str
    code: int
    data: Union[Writer, Publisher, BookAll]


# 查_成功
class GeneralResDefine(BaseModel):
    message: str
    code: int
    data: List[Union[Writer, Publisher, BookAll]]


# 改_成功 删_成功
class GeneralUpdate(BaseModel):
    message: str
    code: int
    data: list
