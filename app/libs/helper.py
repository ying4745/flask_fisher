# ! /usr/bin/env python
# ! -*-coding:utf-8 -*-

__author__ = '左岸'


def is_isbn_or_key(word):
	"""
	判断参数是关键字还是ISBN
	"""
	isbn_or_key = 'key'
	if len(word) == 13 and word.isdigit():
		isbn_or_key = 'isbn'
	short_word = word.replace('-', '')
	if '-' in word and len(short_word) == 10 and short_word.isdigit():
		isbn_or_key = 'isbn'
	return isbn_or_key
