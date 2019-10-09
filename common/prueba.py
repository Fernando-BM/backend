#! /usr/bin/python2.7
import requests
res = requests.post('http://localhost/publibookApi/login', json={"password":"lalala",})
if res.ok:
    print (res.json())
else:
	for respuesta in res:
		print (respuesta)