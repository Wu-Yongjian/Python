from sqlalchemy import create_engine,Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.engine import reflection
from sqlalchemy import UniqueConstraint, Index

engine = create_engine(
    "mysql+pymysql://jian:123456@127.0.0.1:3306/jian?charset=utf8mb4",
    echo=False,  ##if true will oupt all the program executed sql
    max_overflow=5) ## the max connection

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
'''
class jian_message(Base):
    __tablename__ = "jian_message"
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(12))
    age = Column(String(2))
    __table_args__ = (
        # 设置联合唯一
        UniqueConstraint('id', 'name', name='uix_id_name'),

        # 建立索引
        Index('uix_id_name', 'name'),
    )
'''
def init_db():
    """创建所有定义的表到数据库中"""
    Base.metadata.create_all(engine)


def drop_db():
    """从数据库中删除所有定义的表"""
    Base.metadata.drop_all(engine)

def get_table_metadata(tablename):
    query='desc '+ tablename
    tabled=session.execute(query).fetchall()
#    return session.execute(query).fetchall()[0:-1:1]
    return (session.execute(query).fetchall()[0:-1:1])

def get_all_tables():
    return session.execute('show tables').fetchall()

def get_table_data(tablename):
    query = 'select * from ' + tablename
    return session.execute(query).fetchall()

#table_def=get_table_metadata('jian_message')
#print(table_def.fetchall())



#session.add(jian_message(name='cc',age=18))
#session.commit()
#rest=session.query(jian_message).filter(jian_message.id==2).all()
#for i in rest:
# print(i.name)