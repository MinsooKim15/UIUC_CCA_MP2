import requests
import json

url = 'https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp2-autograder-2022-spring'

payload = {
		'ip_address1':  "http://ec2-3-35-14-184.ap-northeast-2.compute.amazonaws.com",
		'ip_address2':  "http://ec2-13-125-83-194.ap-northeast-2.compute.amazonaws.com",
		'load_balancer' :  "my-alb2-10646403.ap-northeast-2.elb.amazonaws.com",
		'submitterEmail':  "minsookim0615@gmail.com",
		'secret':  "CGlYg93GucBEfsjl"
		}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)