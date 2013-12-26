SEU_Web_Login
=============

SEU_Web_Login

This program is a python implement for CLI(command-line interface) web login in Southeast University(China), using httplib and json. The login and logout fuctions are based on portal.js(login and logout javascript) on w.seu.edu.cn.  

Usage:
	
You need to fill your username and password first. Then just excute it with params.

	python seu_weblogin.py [login | logout | status | help]

	-login:
	Login by https. Print ip address.
	
	-logout:
	Logout by https.

	-status:
	Print login time and login ip address. Time format 12:12:12(h:m:s)

Although other methods in linux is more easier, e.g. crul, this program provide the possibility of network authentication(for SEU web login and logout) in python projects. Hoping it will help you.  

For More Information:
http://w.seu.edu.cn


