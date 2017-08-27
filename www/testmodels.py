#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import orm
from models import User, Blog, Comment

def test():
    yield from orm.create_pool(user='www-data', password='www-data', database='awesome')
    u = User(name='Test', email='test@163.com', passwd='123456', image='about:blank')
    yield from u.save()

for x in test():
    pass
