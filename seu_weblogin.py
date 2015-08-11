"""
login and logout w.seu.edu.cn with Python
"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import httplib
import sys
import time
import getpass

USERNAME = 'your_username'
PASSWORD = 'your_password'
HEADERS = {
    'Content-Type': "application/json; charset=utf-8",
    'dataType': "json",
    'cache': False
}
ADDRESS = "w.seu.edu.cn"
INIT_URL = "/portal/init.php"
LOGIN_URL = "/portal/login.php"
LOGOUT_URL = "/portal/logout.php"


def print_result(content):
    """Print response from server.
    Print Username, IP address, Login Time, Login Location
    """
    try:
        if 'error' in content:
            dresq = eval(content.encode('utf-8'))
            # decode utf-8 character
            print "Error:" + unicode(dresq["error"]).decode('unicode-escape')
        else:
            # fuction eval will convert json to dict
            # need to replace 'null' otherwise eval will return error
            dresq = eval(content.replace('null', "'w.seu.edu.cn'").encode('utf-8'))
            # print username & IP address
            print "Username: " + dresq['login_username']
            print "IP Address: " + dresq['login_ip']
            print "Login Time: " + time.strftime('%H:%M:%S', time.gmtime(dresq['login_time']))
            print "Login Location: " + unicode(dresq['login_location']).decode('unicode-escape')
            print "Expire Time: " + unicode(dresq['login_expire']).decode('unicode-escape') + \
                '(remain ' + unicode(dresq['login_remain']).decode('unicode-escape') + ' days)'
    except:
        print "Print error! Maybe something is wrong in UTF-8 encode and json decode"


def login(username, password):
    """Login fuction based on httplib.
    Check login status, if logined then print status (IP, time, location).
    If not logined, 'POST' your login parameters to server.
    """
    conn = httplib.HTTPSConnection(ADDRESS)
    conn.request("GET", INIT_URL, headers=HEADERS)
    # get response from web server
    content = conn.getresponse().read()
    # make sure if user is login
    if 'notlogin' not in content:
        print "Already login!"
        content = content[3:]
        print_result(content)
        return
    params = {'username': username, 'password': password}
    try:
        conn = httplib.HTTPSConnection(ADDRESS)
        conn.request("POST", LOGIN_URL, urllib.urlencode(params), headers=HEADERS)
        # get response from web server
        content = conn.getresponse().read()
        # remove useless header
        content = content[5:]
        print_result(content)
        conn.close()
    except:
        print "Post error!"


def logout():
    """Logout based on httplib.
    'POST' logout parameters to server.
    """
    try:
        conn = httplib.HTTPSConnection(ADDRESS)
        conn.request("POST", LOGOUT_URL, headers=HEADERS)
        conn.close()
        print "Logout Sucess!!"
    except:
        print "Post error!"


def status():
    """Print login status.
    If logined, print status (IP, time, location).
    If not logined, print 'Not login!'
    """
    try:
        conn = httplib.HTTPSConnection(ADDRESS)
        conn.request("GET", INIT_URL, headers=HEADERS)
        # get response from web server
        content = conn.getresponse().read()
        # make sure if user is login
        if 'notlogin' in content:
            print "Not login!"
            return
        # remove useless header, http header here is different from login.
        content = content[3:]
        print_result(content)
    except:
        print "Get Status error!"


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print "No param is inputed. Please input params."
        print "Usage python %s [login | logout | status | help]" % sys.argv[0]
    elif sys.argv[1] == 'login':
        try:
            # for command "python seu_weblogin.py login username password"
            INPUT_USERNAME = sys.argv[2]
            INPUT_PASSWORD = sys.argv[3]
        except IndexError:
            # if you didn't want to save username and password in this file
            # you can input username and password by standard input
            INPUT_USERNAME = USERNAME
            INPUT_PASSWORD = PASSWORD
            if 'your' in USERNAME or 'your' in PASSWORD:
                # reqire username and password from std input
                INPUT_USERNAME = raw_input("Username:")
                # don't show my password on screen
                INPUT_PASSWORD = getpass.getpass("Password:")
        login(INPUT_USERNAME, INPUT_PASSWORD)
    elif sys.argv[1] == 'logout':
        logout()
    elif sys.argv[1] == 'status':
        status()
    else:
        print "Input param is not supported!"
        print "Usage python %s [login | logout | status | help]" % sys.argv[0]
