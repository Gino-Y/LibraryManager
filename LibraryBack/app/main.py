import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from dependencies import get_db

app = FastAPI()


# 创建作者信息
@app.post('/writer', response_model=schemas.Writer)
def create_writer(writer: schemas.WriterCreate, db: Session = Depends(get_db)):
    db_writer = crud.get_writer_by_username(db, writer.username)
    if db_writer:
        raise HTTPException(status_code=400, detail='writer already exists')
    return crud.create_writer(db, writer)


# 获取所有作者信息
@app.get('/writers')
def get_all_writer(db: Session = Depends(get_db)):
    return crud.get_all_writer(db)


# alembic init alembic
if __name__ == '__main__':
    uvicorn.run(app=app, host='127.0.0.1', port=8030)
