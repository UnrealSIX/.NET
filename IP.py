import socket
import os
import urllib.request
import json
import ssl #导入SSL
#获取本机电脑名
myname = socket.getfqdn(socket.gethostname(  ))
#获取本机ip
myaddr = socket.gethostbyname(myname)
print ('本机名：',myname)
print ('内网IP地址：',myaddr)

#获取外网IP
#ssl._create_default_https_context = ssl._create_unverified_context #关闭SSL
#response = urllib.request.urlopen('https://api.ipify.org/?format=json')
response = urllib.request.urlopen('https://jsonip.com/')
js = json.loads(response.read())
print ('外网IP地址：',js['ip'])


os.system('pause')
