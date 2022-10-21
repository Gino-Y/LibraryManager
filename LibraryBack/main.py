from fastapi import FastAPI
import uvicorn

from database import engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
async def home():
    return {'username': 'zhangsan'}


if __name__ == '__main__':
    uvicorn.run(app=app, host='127.0.0.1', port=8030)
