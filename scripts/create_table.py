#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：coding 
@File    ：create_table.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-11-18 16:52 
"""
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, DateTime, func, Boolean, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, backref

engine = create_engine("mysql+pymysql://root:123456@192.168.253.246:3306/3dr_pro", echo=True)
Base = declarative_base()
session = sessionmaker(bind=engine)()


# class RoleBase(Base):
#     """
#     服务表
#     """
#     __tablename__ = 'role_base'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     role_type = Column(String(20), comment="角色类型", default="", nullable=False)
#     role_name = Column(String(20), comment="类型名称", default="", nullable=False)
#     role_level = Column(Integer, comment="类型等级", default=2, nullable=False)
#     created_time = Column(DateTime, nullable=False, server_default=func.now(), default=datetime.now, index=True)
#     updated_time = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
#                           default=datetime.now, index=True)
#     deleted = Column(Boolean, comment="是否删除 false 未删除 true 删除", default=False, nullable=False)


class Service(Base):
    """
    服务表
    """
    __tablename__ = 'service'
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(20), comment="服务编码")
    name = Column(String(20), comment="服务名称")
    platform = Column(String(20), comment="适用平台")
    status = Column(String(20), default="active", comment="状态")
    created_time = Column(DateTime, nullable=False, server_default=func.now(), default=datetime.now, index=True)
    updated_time = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
                          default=datetime.now, index=True)
    deleted = Column(Boolean, comment="是否删除 false 未删除 true 删除", default=False, nullable=False)


class TenantService(Base):
    __tablename__ = 'tenant_service'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tenant_id = Column(Integer, comment="租户id", index=True)
    created_time = Column(DateTime, nullable=False, server_default=func.now(), default=datetime.now, index=True)
    updated_time = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
                          default=datetime.now, index=True)
    deleted = Column(Boolean, comment="是否删除 false 未删除 true 删除", default=False, nullable=False)
    service_id = Column(Integer, ForeignKey('service.id'), comment="服务id", index=True)
    service = relationship(Service, backref=backref('b_a'), lazy='dynamic')

def main():

    pass


def test_sql():
    result = session.query(TenantService).all()
    print(result)
    # print(result.service)



if __name__ == "__main__":
    test_sql()
