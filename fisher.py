# ! /usr/bin/env python
# ! -*-coding:utf-8 -*-
from app import create_app

__author__ = '左岸'

app = create_app()

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
