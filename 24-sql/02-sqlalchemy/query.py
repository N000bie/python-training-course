# -*- encoding: utf-8 -*-
from pprint import pprint

import model
from db import get_session

import logger

logger.enable_sql_log()


def flatten_record(r):
    if isinstance(r, list):
        l = [
            flatten_record(ele) for ele in r
        ]
        return l
    else:
        d = {
            c.key: getattr(r, c.key) for c in r.__table__.c
        }
        return d


def print_record(r):
    pprint(flatten_record(r), indent=2)


session = get_session()

print('emp2 info:')
print('.' * 40)
emp2 = session.query(model.Employee).get(2)
print_record(emp2)
print('.' * 40, '\n')

print('emp2 department info:')
print('.' * 40)
print_record(emp2.department)
print('.' * 40, '\n')

print('emp2 managees:')
print('.' * 40)
print_record(emp2.managees)
print('.' * 40, '\n')

print('emp2 manager info:')
print('.' * 40)
print_record(emp2.manager)
print('.' * 40, '\n')

print('new york employees I')
print('.' * 40)
new_york_depts = session.query(model.Department).filter(
    model.Department.loc == 'NEW YORK'
).all()
for dept in new_york_depts:
    print_record(dept.employees)
print('.' * 40, '\n')

print('new york employees II')
print('.' * 40)
new_york_employees = session.query(model.Employee).filter(
    model.Employee.department.has(
        model.Department.loc == 'NEW YORK'
    )
).all()
print_record(new_york_employees)
print('.' * 40, '\n')

print('new york employees III')
print('.' * 40)
new_york_employees = session.query(model.Employee).join(
    model.Department
).filter(
    model.Department.loc == 'NEW YORK'
).all()
print_record(new_york_employees)
print('.' * 40, '\n')
