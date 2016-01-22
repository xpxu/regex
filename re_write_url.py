# -*- coding:utf-8 -*-
'''
Purpose: Filtering Nimbula APIs using Apache Proxy
--------------------------------------
RewriteCond /federation/@SITENAME@/vpnendpoint/,%{REQUEST_URI} ^([^,]+),\1
RewriteRule ^/(.*) balancer://api%{REQUEST_URI} [P]
注：比较前面的字符串和后面的正则表达式，看是否匹配。如果匹配，那么
执行RewriteRule，将前面正则表达式匹配的url重写成后面的url.
--------------------------------------
RewriteRule replace the Nimbula API IP in place of Apache proxy IP.
'''

import re

def is_match(str, reg):
    '''
    match str with reg
    '''
    if re.match(reg, str):
        print 'match ok'
    else:
        print 'match failed'

def test1():
    input = '010-123'
    reg = r'^\d{3}\-\d{3,8}$'
    is_match(input, reg)

def test2():
    input = ',federation,federation'
    # this reg means the checked string should be
    # start not with ',', if so, it's OK.
    reg = r'^([^,]+)'
    is_match(input, reg)


def test3():
    input = 'federation,federationxx'
    # this reg means the checked string should be
    # start like 'something,somethingxxx'
    reg = r'^([^,]+),\1'
    is_match(input, reg)

def test4():
    input = 'federation,ederationxx'
    # this reg means the checked string should be
    # start like 'something,somethingxxx'
    reg = r'^([^,]+),\1'
    is_match(input, reg)

test4()
