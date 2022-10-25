from datetime import datetime

from pydantic import BaseModel, EmailStr
from typing import Optional


class WriterBase(BaseModel):
    username: str


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


# 出版社响应体校验
class Publisher(PublisherBase):
    id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    price: float
    publisher_data: Optional[datetime] = None


# 书籍请求体校验模型
class BookCreate(BookBase):
    pass


# 书籍响应体校验模型
class Book(BookBase):
    writer_id: int

    class Config:
        orm_mode = True


# 自定義作者創建成功響應躰的校驗模型
class GeneralDefine(BaseModel):
    message: str
    code: int
    obj: Writer




