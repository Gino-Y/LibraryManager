from pydantic import BaseModel, EmailStr


class WriterBase(BaseModel):
    username: str


# 作者请求体校验
class WriterCreate(WriterBase):
    email: EmailStr


# 作者响应体校验
class Writer(WriterBase):
    id: int
    email: EmailStr

    class config:
        orm_mode = True
