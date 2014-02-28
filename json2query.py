#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
