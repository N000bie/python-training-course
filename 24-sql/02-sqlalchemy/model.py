# -*- encoding: utf-8 -*-
from sqlalchemy import Column, Integer, Unicode, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship, backref

from db import Base


class Employee(Base):
    __tablename__ = 'emp'
    empno = Column(Integer, nullable=False, primary_key=True)
    ename = Column(Unicode(10))
    job = Column(Unicode(9))

    mgr = Column(Integer, ForeignKey('emp.empno'))
    manager = relationship(
        'Employee', uselist=False,
        remote_side=[empno,],
        backref=backref('managees')
    )

    hiredate = Column(DateTime(timezone=False))
    sal = Column(DECIMAL(7, 2))
    comm = Column(DECIMAL(7, 2))

    dept = Column(Integer, ForeignKey('dept.deptno'))
    department = relationship(
        'Department', uselist=False,
        backref=backref('employees')
    )


class Department(Base):
    __tablename__ = 'dept'
    deptno = Column(Integer, nullable=False, primary_key=True)
    dname = Column(Unicode(14))
    loc = Column(Unicode(13))
