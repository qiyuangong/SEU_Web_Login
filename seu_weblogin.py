#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import httplib
import json
import sys
import time

gl_username = 'your_username'
gl_password = 'your_password'

headers = {
	'Content-Type': "application/json; charset=utf-8",
	'dataType': "json",
	'cache': False
	}
url = "w.seu.edu.cn"
init_url = "/portal/init.php"
login_url = "/portal/login.php"
logout_url = "/portal/logout.php"

def print_result(content):
	'''Print response from server.'''
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
			print "Username: " + gl_username
			print "IP Address: " + dresq['login_ip']
			print "Login Time: " + time.strftime('%H:%M:%S', time.gmtime(dresq['login_time']))
			print "Login Location: " + unicode(dresq['login_location']).decode('unicode-escape')
	except:
		print "Print error! Maybe something is wrong in UTF-8 encode and json decode"

def login(username, password):
	'''Login fuction based on httplib. "POST" your login parameters to server.'''
	global headers, login_url, url, init_url

	conn = httplib.HTTPSConnection(url)
	conn.request("GET", init_url, headers=headers)
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
		conn = httplib.HTTPSConnection(url)
		conn.request("POST", login_url, urllib.urlencode(params), headers=headers)
		#get response from web server
		content = conn.getresponse().read()
		# remove useless header
		content = content[5:]
		print_result(content)
		conn.close()
	except:
		print "Post error!"

def logout():
	'''Logout based on httplib. "POST" logout parameters to server.'''
	global headers, url, logout_url
	try:
		conn = httplib.HTTPSConnection(url)
		conn.request("POST", logout_url, headers=headers)
		conn.close()
		print "Logout Sucess!!"
	except:
		print "Post error!"

def status():
	'''Print login status (IP, time, location). If not login, print "Not login!"'''
	global headers, url, index_url
	try:
		conn = httplib.HTTPSConnection(url)
		conn.request("GET", init_url, headers=headers)
		#get response from web server	
		content = conn.getresponse().read()
		# make sure if user is login 
		if 'notlogin' in content:
			print "Not login!"
			return
		# remove useless header
		# Head here is different from login.
		content = content[3:]
		print_result(content)
	except:
		print "Get Status error!"

'''
def login_basedon_request(username, password):
	"login code base on requests(lib), which need installation"
	import requests
	URL = 'https://w.seu.edu.cn/portal/login.php'
	# params = {'username': unicode(username).encode('utf-8'), 'password': unicode(password).encode('utf-8')}
	params = {'username': username, 'password': password}
	resq = requests.post(URL, data=urllib.urlencode(params), allow_redirects=True, headers=headers)
	content = resq.text 
	print_result(content)
'''

if __name__ == '__main__':

	if len(sys.argv) <= 1:
		print "No param is inputed. Please input params."
		print "Usage python %s [login | logout | status | help]" % sys.argv[0]
	elif sys.argv[1] == 'login':
		login(gl_username, gl_password)
	elif sys.argv[1] == 'logout':
		logout()
	elif sys.argv[1] == 'status':
		status()
	else:
		print "Input param is not supported!"
		print "Usage python %s [login | logout | status | help]" % sys.argv[0]
