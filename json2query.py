#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
echo '{ "title": "Бумажки: простая игра на сегодняшний вечер / Блог компании Мосигра / Хабрахабр", "url": "http://habrahabr.ru/company/mosigra/blog/207906/" }' | python json2query.py | pbcopy
echo '{ "post": { "title": "Бумажки: простая игра на сегодняшний вечер / Блог компании Мосигра / Хабрахабр", "url": "http://habrahabr.ru/company/mosigra/blog/207906/" }}' | python json2query.py | pbcopy
curl -d'url=http%3A%2F%2Fhabrahabr.ru%2Fcompany%2Fmosigra%2Fblog%2F207906%2F&title=%D0%91%D1%83%D0%BC%D0%B0%D0%B6%D0%BA%D0%B8%3A+%D0%BF%D1%80%D0%BE%D1%81%D1%82%D0%B0%D1%8F+%D0%B8%D0%B3%D1%80%D0%B0+%D0%BD%D0%B0+%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F%D1%88%D0%BD%D0%B8%D0%B9+%D0%B2%D0%B5%D1%87%D0%B5%D1%80+%2F+%D0%91%D0%BB%D0%BE%D0%B3+%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B8+%D0%9C%D0%BE%D1%81%D0%B8%D0%B3%D1%80%D0%B0+%2F+%D0%A5%D0%B0%D0%B1%D1%80%D0%B0%D1%85%D0%B0%D0%B1%D1%80' http://localhost:3333/page
"""

import sys
import urllib
import json

def _generate_list(source, sub_field):
    r = []
    for i, row in enumerate(source):
        key = "%s[%d]" % (sub_field, i)
        if isinstance(row, dict):
            r.append(_generate_dict(row, key))
        elif isinstance(row, basestring):
            r.append("%s=%s" % (urllib.quote(key), urllib.quote(row.encode('utf8'))))
    return "&".join(r)

def _generate_dict(source, sub_field=None):
    r = []
    for field, row in source.iteritems():
        if isinstance(row, list):
            r.append(_generate_list(row, field))
        elif isinstance(row, dict):
            r.append(_generate_dict(row, field))
        elif isinstance(row, basestring):
            if sub_field:
                field = "%s[%s]" % (sub_field, field)

            if isinstance(row, str):
                row = row.decode('utf-8')

            r.append("%s=%s" % (urllib.quote(field), urllib.quote(row.encode('utf8'))))
    return "&".join(r)

def generate(source):
    if isinstance(source, list):
        raise Exception("Must be a dictionary")

    if isinstance(source, str):
        try:
            source = json.loads(source)
        except:
            raise Exception("String isn't json or doesn't valid")

    return _generate_dict(source)

def main(source):
    return generate(json.loads(source))

if __name__ == '__main__':
    print main(sys.stdin.read())
