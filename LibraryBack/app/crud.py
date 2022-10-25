from sqlalchemy.orm import Session

import schemas
from app.models.models import Writer, Book, Publish, Match
# from app.models import models
# models,虽然这样写是没问题的，但是安装规范是和我下面写的那样，之前的主要问题可能就是你app放在了alembic里面,导致报错了，移出来就好了，这里是我顺手改的
#还有那个models文件夹也没啥东西，只是看的清楚一些，规范
# user_info = db.query(models.Writer).filter(models.Writer.username == username).first()


def get_writer_by_username(db: Session, username: str):
    user_info=db.query(Writer).filter(Writer.username == username).first()
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