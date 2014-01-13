SEU_Web_Login
=============

This program is a python implement for CLI (command-line interface) web login in Southeast University (China). The whole script is based on **httplib** and **json** (I also add a fuction based on requests lib, which need extra package). The login and logout fuctions are based on **portal.js** (login and logout javascript) on w.seu.edu.cn.  

## Usage:
	
You need to fill your username and password first. 

	# replace with your username and password
	gl_username = 'your_username' 
	gl_password = 'your_password' 

Then just excute it with params.

	python seu_weblogin.py [login | logout | status | help]

	-login:
	Login by https. Print ip address.
	
	-logout:
	Logout by https.

	-status:
	Print login time, login location and login ip address. Time format 12:12:12(h:m:s).

	-help:
	Print usage.

Although other methods in linux is more easier, e.g. crul. Shell command for crul :

	# replace with your username and password
	curl -3 'https://w.seu.edu.cn/portal/login.php' -d 'username=your_username' -d  'password=your_password'

This program provide the possibility of network authentication (for SEU web login and logout) in python projects. **Hoping it will help you.**

## For More Information:
http://w.seu.edu.cn

### Feedback:
qiyuangong@gmail.com
