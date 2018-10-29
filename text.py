# ! /usr/bin/env python
# ! -*-coding:utf-8 -*-

__author__ = '左岸'

# 实现上下文管理器
class MyResource:
    # def __enter__(self):
    #     print('connect to resource')
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     print('close resource connection')

    def query(self):
        print('query data')

# 应用
# with MyResource() as r:
#     r.query()

# 简化定义上下文管理器
from contextlib import contextmanager

@contextmanager
def make_myresource():
    print('connect to resource')
    yield MyResource()
    print('close resource connection')

with make_myresource() as r:
    r.query()

# 代码的执行流程：先执行__enter__下的print('connect to resource')
# 然后上下文管理器返回回去，返回回去r才是要操作的对象，才可以执行with
# 下的r.query()，执行完后，再执行 __exit__下的
# print('close resource connection')

# 灵活应用 -为书名前后打印《》
@contextmanager
def book_mark():
    print('《', end='')
    yield
    print('》', end='')

with book_mark():
    print('一江春水', end='')
