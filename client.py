import requests
import time
data1 = 12
data2 = 54
str = "Hi"

session = requests.Session()
session.headers.update({'User-Agent': 'Custom user agent'})
res = session.post("http://127.0.0.1:8000/", data="{" + f"'data1':{12},'data2':{54},'data3':'{str}'" + "}")
print(res)
