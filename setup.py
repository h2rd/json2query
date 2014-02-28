#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Json to query url
-----------------

    echo '{ "title": "Бумажки: простая игра на сегодняшний вечер / Блог компании Мосигра / Хабрахабр", "url": "http://habrahabr.ru/company/mosigra/blog/207906/" }' | json2query | pbcopy
    echo '{ "post": { "title": "Бумажки: простая игра на сегодняшний вечер / Блог компании Мосигра / Хабрахабр", "url": "http://habrahabr.ru/company/mosigra/blog/207906/" }}' | json2query | pbcopy

"""

from setuptools import setup

setup(
    name='json2query',
    author='Igor Skrynkovskyy',
    author_email='skrynkovskyy@gmail.com',
    description='Json to query url',
    long_description=__doc__,
    license="MIT",
    url='Json to query url',
    version='0.1',
    py_modules=['json2query'],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'json2query = json2query:main',
            'j2q = json2query:main']
    }
)
