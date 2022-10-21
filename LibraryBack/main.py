from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
async def home():
    return {'username': 'zhangsan'}


if __name__ == '__main__':
    print('hello world')