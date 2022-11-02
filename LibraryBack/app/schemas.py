"""
数据校验
"""
from datetime import datetime

from pydantic import BaseModel, EmailStr
from typing import Optional, List, Union


class WriterBase(BaseModel):
    username: str


# 作者请求体校验
class WriterCreate(WriterBase):
    email: EmailStr


# 作者响应体校验，需要id及email，这里也是满足的id和email
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
class BookCreate(BookBase):
    pass


# 书籍响应体校验模型，需要返回参数里面有这个weriterid,这个是有的
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
    # Writer需要的
    # id: int
    # email: EmailStr
    publishers: List[Publisher]
    # 这个是一个list类型也没错，然后下标0里面存在id
    # Publisher需要的但是他外面还有一个list所以他2还需要是list的格式的然后里面才有id
    # id: int，是不是和这些都一样都有的


# 自定義創建成功響應躰的校驗模型，然后要求格式下面这三个格式，然后data里面的校验格式要按照这里面三个来，所以weriter里面需要id和email，Publisher，里面需要id，
# BookAll里面是需要上面这些信息，然后里面的内容按照所对应都要求格式就好了，现在res里面是不是就是msg code data三个，所以就符合了，然后再看里面，这
# 样就都满足了，就返回成功了
class GeneralDefine(BaseModel):
    message: str
    code: int
    data: Union[Writer, Publisher, BookAll]
#     然后这里data也是三个满足一个就好了应该


# 自定义获取所有作者成功响应体校验模型
class GeneralResDefine(BaseModel):
    message: str
    code: int
    data: List[Union[Writer, Publisher, BookAll]]
