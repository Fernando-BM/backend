#! /usr/bin/python2.7
import requests
res = requests.post('http://localhost/proyecto/login', json={"correo":"abalsdon4@artisteer.com","contasenia":"wAsxndekX"})
if res.ok:
    print (res.json())
else:
	for respuesta in res:
		print (respuesta)
