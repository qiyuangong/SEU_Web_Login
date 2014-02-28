SEU_Web_Login
=============

This program is a python implement for CLI (command-line interface) web login in Southeast University (China). The whole script is based on **httplib** and **json** (I also add a fuction based on requests lib, which need extra package). The login and logout fuctions are based on **portal.js** (login and logout javascript) on w.seu.edu.cn.

本程序用于命令行内进行东南大学Web认证（认证上网或者登出）。程序基于python 的**httplib** and **json**库，通过https提交完成登录和退出。提交格式参照，w.seu.edu.cn的登录脚本**portal.js**。 

## Usage:
	
You need to fill your username and password first. 

使用前，请替换用户名和密码：

	# replace with your username and password
	gl_username = 'your_username' 
	gl_password = 'your_password' 

Then just excute it with params.

运行参数如下：login-登录 logout-退出 status-查看在线状态 help-打印帮助

	python seu_weblogin.py [login | logout | status | help]

	-login:
	Login by https. Print ip address.
	
	-logout:
	Logout by https.

	-status:
	Print login time, login location and login ip address. Time format 12:12:12(h:m:s).

	-help:
	Print usage.

Although other methods in linux is more easier, e.g. crul. Shell command for crul:

当然，其实linux用户可以用curl来登录和退出web认证（只是不能查看状态）：

	# replace with your username and password
	curl -3 'https://w.seu.edu.cn/portal/login.php' -d 'username=your_username' -d  'password=your_password'

This program provide the possibility of network authentication (for SEU web login and logout) in python projects. **Hoping it will help you.**


## For More Information:
http://w.seu.edu.cn

### Feedback:
qiyuangong@gmail.com
