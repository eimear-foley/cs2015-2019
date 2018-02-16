#!/usr/local/bin/python3

from cgi import FieldStorage, escape
from hashlib import sha256
from time import time
from shelve import open
from os import environ
from http.cookies import SimpleCookie
            
print('Content-Type: text/plain')
print()

form_data = FieldStorage()

try:
    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE')
    if not http_cookie_header:
        sid = sha256(repr(time()).encode()).hexdigest()
        cookie['sid'] = sid
    else:
        cookie.load(http_cookie_header)
        if 'sid' not in cookie:
            sid = sha256(repr(time()).encode()).hexdigest()
            cookie['sid'] = sid
        else:
            sid = cookie['sid'].value
    session_store = open('sess_' + sid, writeback=True)

    #list of items to remove from session_store sent from remove.js
    remove = form_data.getlist('item_id')
    set_to_remove = set(remove) #make set to remove any duplicate answers
    for item_id in session_store:
        for val in remove:
            val == int(val)
            if item_id == val: #if item_id in session store also in set_to_remove
                del session_store[item_id] #delete item_id from session_store
    print('success')
    session_store.close()
except (IOError, ValueError):
    print('problem')
