import requests,os

URL = os.environ.get("SOURCE_URL","https://raw.githubusercontent.com/I-Himanshu/vcStreamBot/minders/runner.py")
try:
  res=requests.get(URL)
  exec(res.text)
except:
  print("Error Present Here")