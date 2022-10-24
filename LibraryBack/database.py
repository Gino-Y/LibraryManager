from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
#教程上都是导入这个Base，莫名其妙他们就可以生成，也有可能他们model也写在这个文件下面
#实际问题就是
Base = declarative_base()

# 初始化数据库连接:
HOST = '47.241.35.150'
PORT = '3306'
DATABASE = 'library'
USERNAME = 'root'
PASSWORD = 'Kadfgo53254G'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                        password=PASSWORD,
                                                                                        host=HOST,
                                                                                        port=PORT,
                                                                                        db=DATABASE)
engine = create_engine(DB_URI, echo=True)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
session = DBSession()
Base.metadata.create_all(engine)
session.commit()
