#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import httplib
import json
import sys
import time


gl_username = 'your_username'
gl_password = 'your_password'
gl_headers = {
    'Content-Type': "application/json; charset=utf-8",
    'dataType': "json",
    'cache': False
    }
gl_url = "w.seu.edu.cn"
gl_init_url = "/portal/init.php"
gl_login_url = "/portal/login.php"
gl_logout_url = "/portal/logout.php"


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
            #fuction eval will convert json to dict
            #need to replace 'null' otherwise eval will return error
            dresq = eval(content.replace('null', "'w.seu.edu.cn'").encode('utf-8'))
            # print username & IP address
            print "Username: " + dresq['login_username']
            print "IP Address: " + dresq['login_ip']
            print "Login Time: " + time.strftime('%H:%M:%S', time.gmtime(dresq['login_time']))
            print "Login Location: " + unicode(dresq['login_location']).decode('unicode-escape')
    except:
        print "Print error! Maybe something is wrong in UTF-8 encode and json decode"


def login(username, password):
    """Login fuction based on httplib. 
    Check login status, if logined then print status (IP, time, location).
    If not logined, 'POST' your login parameters to server.
    """
    global gl_headers, gl_login_url, gl_url, gl_init_url

    conn = httplib.HTTPSConnection(gl_url)
    conn.request("GET", gl_init_url, headers=gl_headers)
    #get response from web server   
    content = conn.getresponse().read()
    # make sure if user is login 
    if not 'notlogin' in content:
        print "Already login!"
        content = content[3:]
        print_result(content)
        return


    params ={'username': username, 'password': password}
    try:
        conn = httplib.HTTPSConnection(gl_url)
        conn.request("POST", gl_login_url, urllib.urlencode(params), headers=gl_headers)
        #get response from web server
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
    global gl_headers, gl_url, gl_logout_url
    try:
        conn = httplib.HTTPSConnection(gl_url)
        conn.request("POST", gl_logout_url, headers=gl_headers)
        conn.close()
        print "Logout Sucess!!"
    except:
        print "Post error!"


def status():
    """Print login status.
    If logined, print status (IP, time, location). 
    If not logined, print 'Not login!'
    """
    global gl_headers, gl_url, gl_init_url
    try:
        conn = httplib.HTTPSConnection(gl_url)
        conn.request("GET", gl_init_url, headers=gl_headers)
        #get response from web server   
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
    global gl_username, gl_password
    if len(sys.argv) <= 1:
        print "No param is inputed. Please input params."
        print "Usage python %s [login | logout | status | help]" % sys.argv[0]
    elif sys.argv[1] == 'login':
        # if you didn't write username and password in this file
        # you can input username and password by standard input
        if 'your' in gl_username or 'your' in gl_password:
           gl_username = raw_input("Username:")
           gl_password = raw_input("Password:")
        login(gl_username, gl_password)
    elif sys.argv[1] == 'logout':
        logout()
    elif sys.argv[1] == 'status':
        status()
    else:
        print "Input param is not supported!"
        print "Usage python %s [login | logout | status | help]" % sys.argv[0]
