from urllib import request

import uvicorn
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Union
import crud
import schemas
from dependencies import get_db

origins = [
    "http://0.0.0.0",
    "http://0.0.0.0:8030",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 曾 一 作者
@app.post('/create_writer', response_model=Union[schemas.Writer, schemas.GeneralDefine])
async def create_writer(writer: schemas.WriterCreate, db: Session = Depends(get_db)):
    res = {
        'message': '創建成功',
        'code': 200,
        'data': {}
    }
    db_writer = crud.get_writer_by_username(db, writer.username)
    if db_writer:
        res['message'] = '当前作者已记录'
        raise HTTPException(status_code=400, detail='writer already exists')
    try:
        result = crud.create_writer(db, writer)
        res['data'] = result
    except Exception as e:
        res['message'] = '創建失敗'
        res['code'] = 208
    return res


# 删 一 作者
@app.get('/delete_writer', response_model=schemas.GeneralUpdate)
async def delete_writer(id=Query(), db: Session = Depends(get_db)):
    res = {
        'message': '删除成功',
        'code': 200,
        'data': []
    }
    try:
        result = crud.writer_delete(db, id)
    except:
        res['message'] = '删除失败'
        res['code'] = 208
    return res


# 查 多 作者
@app.get('/get_all_writer', response_model=Union[List[schemas.Writer], schemas.GeneralResDefine])
async def get_all_writer(db: Session = Depends(get_db)):
    res = {
        'message': '获取成功',
        'code': 200,
        'data': []
    }
    try:
        result = crud.get_all_writer(db)
        res['data'] = result
    except:
        res['message'] = '获取失败'
        res['code'] = 208
    return res


# 曾 一 出版社
@app.post('/create_publisher', response_model=Union[schemas.Publisher, schemas.GeneralDefine])
async def create_publisher(publisher: schemas.PublisherCreate, db: Session = Depends(get_db)):
    res = {
        'message': '创建成功',
        'code': 200,
        'data': []
    }
    db_publisher = crud.get_publisher_by_name(db, publisher.name)
    if db_publisher:
        res['message'] = '当前出版社已记录'
        raise HTTPException(status_code=400, detail='publisher already exists')
    try:
        result = crud.create_publisher(db, publisher)
        res['data'] = result
    except:
        res['message'] = '创建失败'
        res['code'] = 208
    return res


# 删 一 出版社
@app.get('/delete_publisher', response_model=schemas.GeneralUpdate)
async def delete_book(id=Query(), db: Session = Depends(get_db)):
    res = {
        'message': '删除成功',
        'code': 200,
        'data': []
    }
    try:
        result = crud.publisher_delete(db, id)
    except:
        res['message'] = '删除失败'
        res['code'] = 208
    return res


# 改 一 出版社
@app.post('/updata_publisher', response_model=schemas.GeneralUpdate)
async def updata_publisher(publisher: schemas.BookCreate, db: Session = Depends(get_db)):
    res = {
        'message': '修改成功',
        'code': 200,
        'data': []
    }
    try:
        result = crud.publisher_update(db, publisher)
        # res['data'] = result
    except:
        res['message'] = '修改失败'
        res['code'] = 208
    return res


# 查 多 出版社
@app.get('/get_all_publisher', response_model=Union[List[schemas.Publisher], schemas.GeneralResDefine])
async def get_all_publisher(db: Session = Depends(get_db)):
    res = {
        'message': '获取成功',
        'code': 200,
        'data': []
    }
    try:
        result = crud.get_all_publisher(db)
        res['data'] = result
    except:
        res['message'] = '获取失败'
        res['code'] = 208
    return res


# 曾 一 书籍
@app.post('/create_book', response_model=Union[schemas.Book, schemas.GeneralDefine])
async def create_book(Book: schemas.BookCreate, db: Session = Depends(get_db)):
    book = Book.book
    writer_id = Book.writer_id
    publisher_id_list = Book.publisher_id_list
    res = {
        'message': '创建成功',
        'code': 200,
        'data': []
    }
    db_book = crud.get_book_by_title(db, book.title)
    if db_book:
        res['message'] = '当前出版社已记录'
        # return db_book
        raise HTTPException(status_code=400, detail='book already exists')
    try:
        result = crud.create_book_by_writer(db, book, writer_id, publisher_id_list)
        res['data'] = result
    except:
        res['message'] = '创建失败'
        res['code'] = 208
    return res


# 删 一 书籍
@app.get('/delete_book', response_model=schemas.GeneralUpdate)
async def delete_book(id=Query(), db: Session = Depends(get_db)):
    res = {
        'message': '删除成功',
        'code': 200,
        'data': []
    }
    try:
        result = crud.book_delete(db, id)
    except:
        res['message'] = '删除失败'
        res['code'] = 208
    return res


# 改 一 书籍
@app.post('/updata_book', response_model=schemas.GeneralUpdate)
async def updata_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    res = {
        'message': '修改成功',
        'code': 200,
        'data': []
    }
    try:
        result = crud.book_update(db, book)
        # res['data'] = result
    except:
        res['message'] = '修改失败'
        res['code'] = 208
    return res


# 查 多 书籍
@app.get('/get_all_book', response_model=schemas.GeneralResDefine)
async def get_all_book(db: Session = Depends(get_db)):
    res = {
        'message': '获取成功',
        'code': 200,
        'data': []
    }
    try:
        result = crud.get_all_books(db)
        res['data'] = result
    except:
        res['message'] = '获取失败'
        res['code'] = 208
    return res


# 初始化
# alembic init alembic
# 生成数据库迁移文件
# alembic revision --autogenerate -m "generate tables"
# 迁移文件映射到数据库
# alembic upgrade head
if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8030)
