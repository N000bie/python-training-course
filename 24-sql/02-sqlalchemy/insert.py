# -*- encoding: utf-8 -*-
import model
from db import get_session

employees = [
    (9, 'JACKSON', 'CEO', None, '01-01-1990', 75000, None, 4),
    (2, 'HARDING', 'MANAGER', 9, '02-02-1998', 52000, 300, 3),
    (6, 'GARFIELD', 'MANAGER', 9, '05-01-1993', 54000, None, 4),
    (10, 'FILLMORE', 'MANAGER', 9, '08-09-1994', 56000, None, 2),
    (14, 'ROOSEVELT', 'CPA', 9, '10-12-1995', 35000, None, 1),
    (3, 'TAFT', 'SALES I', 2, '01-02-1996', 25000, 500, 3),
    (4, 'HOOVER', 'SALES I', 2, '04-02-1990', 27000, None, 3),
    (1, 'JOHNSON', 'ADMIN', 6, '12-17-1990', 18000, None, 4),
    (5, 'LINCOLN', 'TECH', 6, '06-23-1994', 22500, 1400, 4),
    (7, 'POLK', 'TECH', 6, '09-22-1997', 25000, None, 4),
    (12, 'WASHINGTON', 'ADMIN', 6, '04-16-1998', 18000, None, 4),
    (8, 'GRANT', 'ENGINEER', 10, '03-30-1997', 32000, None, 2),
    (11, 'ADAMS', 'ENGINEER', 10, '03-15-1996', 34000, None, 2),
    (13, 'MONROE', 'ENGINEER', 10, '12-03-2000', 30000, None, 2),
]

departments = [
    (1, 'ACCOUNTING', 'ST LOUIS'),
    (2, 'RESEARCH', 'NEW YORK'),
    (3, 'SALES', 'ATLANTA'),
    (4, 'OPERATIONS', 'SEATTLE'),
]


session = get_session()


for deptno, dname, loc in departments:
    session.add(model.Department(
        deptno=deptno, dname=dname, loc=loc
    ))


for empno, ename, job, mgr, hiredate, sal, comm, dept in employees:
    session.add(model.Employee(
        empno=empno, ename=ename, job=job,
        mgr=mgr, hiredate=hiredate, sal=sal,
        comm=comm, dept=dept
    ))

session.commit()