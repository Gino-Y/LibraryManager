import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Union
import crud
import schemas
from dependencies import get_db

app = FastAPI()


# 创建作者信息
@app.post('/writer', response_model=Union[schemas.Writer, schemas.GeneralDefine])
def create_writer(writer: schemas.WriterCreate, db: Session = Depends(get_db)):
    res = {
        'message': '創建成功',
        'code': 200,
        'obj': {}
    }
    db_writer = crud.get_writer_by_username(db, writer.username)
    if db_writer:
        raise HTTPException(status_code=400, detail='writer already exists')
    try:
        obj = crud.create_writer(db, writer)
        res['obj'] = obj
    except Exception as e:
        res['message'] = '創建失敗'
        res['code'] = 208
    return res


# 获取所有作者信息
@app.get('/writers', response_model=List[schemas.Writer])
def get_all_writer(db: Session = Depends(get_db)):
    res = crud.get_all_writer(db)
    return res


# 创建一个出版社信息
@app.post('/publisher', response_model=schemas.Publisher)
def create_publisher(publisher: schemas.PublisherCreate, db: Session = Depends(get_db)):
    db_publisher = crud.get_publisher_by_name(db, publisher.name)
    if db_publisher:
        raise HTTPException(status_code=400, detail='publisher already exists')
    res = crud.create_publisher(db, publisher)
    return res


# 获取所有出版社信息
@app.get('/publishers', response_model=List[schemas.Publisher])
def get_all_publishers(db: Session = Depends(get_db)):
    res = crud.get_all_publisher(db)
    return res


# 创建书籍信息
@app.post('/book/{writer_id}', response_model=schemas.Book)
def create_book(writer_id: int, publisher_id_list: List[int], book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_title(db, book.title)
    if db_book:
        return HTTPException(status_code=400, detail='book already exists')
    res = crud.create_book_by_writer(db, book, writer_id, publisher_id_list)
    return res


# 獲取所有的書籍
@app.get('/books')
def get_all_book(db: Session = Depends(get_db)):
    res = crud.get_all_books(db)
    return res


# 初始化
# alembic init alembic
# 生成数据库迁移文件
# alembic revision --autogenerate -m "generate tables"
# 迁移文件映射到数据库
# alembic upgrade head
if __name__ == '__main__':
    uvicorn.run(app=app, host='127.0.0.1', port=8030)
