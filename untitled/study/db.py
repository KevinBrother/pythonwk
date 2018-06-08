#_*_coding:utf-8_*_

# mysql 普通连接操作
# import mysql.connector
#
# conn = mysql.connector.connect(user='root', password='qwer1234', database='pyDb', use_unicode=True)
# cursor = conn.cursor()
#
# cursor.execute('create table cust (id VARCHAR(20) PRIMARY KEY , name VARCHAR (20))')
#
# cursor.execute('insert into cust (id, name) VALUES (%s, %s)', ['1', 'Wihte'])
#
# conn.commit()
# cursor.close()


# cursor = conn.cursor()
# cursor.execute('select * from cust WHERE id = %s', ('1',))
# print cursor.fetchall()
# print cursor.rowcount
#
# cursor.close()
# conn.close()


#使用 ORM技术  Object-Relational Mapping

# from sqlalchemy import Column, String, create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
# # 创建对象的基类:
# Base = declarative_base()
#
# # 定义User对象:
# class Cust(Base):
#     # 表的名字:
#     __tablename__ = 'cust'
#
#     # 表的结构:
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#
# # 初始化数据库连接
# engine = create_engine('mysql+mysqlconnector://root:qwer1234@localhost:3306/pyDb')
#
# # 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)


# # 创建session对象:
# session = DBSession()
# # 创建新User对象:
# new_cust = Cust(id='3', name='Bob')
# # 添加到session:
# session.add(new_cust)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()


# 创建Session:
# session = DBSession()
# # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
# #     session.query(User).filter(User.id=='5').one()
# cust = session.query(Cust).filter(Cust.id=='5').one()
# # 打印类型和对象的name属性:
# print 'type:', type(cust)
# print 'cust:', cust
#
# print 'name:', cust.name
# # 关闭Session:
# session.close()




