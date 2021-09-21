from telegram import InlineKeyboardMarkup,InlineKeyboardButton,Bot
import time
TOKEN="1816572959:AAGfMjWNxzDsEBdRp8Ovkkat8eqxNvicCJw"
chat_id=-1001492870356
chat_id = -1001557278807
from_chat=1797416707
bot=Bot(TOKEN)
#bot2=Bot("1718858814:AAHWjcYiN6VdQ7dplZhPgD7mGMRcQXtGmt8")
bot2=Bot("1496237028:AAEXDzYf3k1KwkXEpfPi2biRMvONfW9TYkU")
quotes=[]
with open("quotes.json","r") as f:
  import json
  quotes=json.load(f)
k=0
for i in range(500):
  try:
    if abs(k-len(quotes))<5:
      k=0
    print(bot2.sendMessage(chat_id,"Jai Shree Ram🚩").message_id)
    print(bot.copyMessage(chat_id,from_chat,4).message_id)
    print(bot.copyMessage(chat_id,from_chat,5).message_id)
    print(bot2.sendMessage(chat_id,"Har Har Mahadev 🚩").message_id)
    print(bot2.sendMessage(chat_id, quotes[k]).message_id)
    k+=1
    print(bot.copyMessage(chat_id,from_chat,7).message_id)
    print(bot.sendMessage(chat_id, quotes[k]).message_id)
    k+=1
    print(bot2.sendMessage(chat_id,"Jai Bajrang Bali").message_id)
  except Exception as e:
    try:
      print("Error Occurred",e)
      print(bot2.sendMessage(chat_id, quotes[k]).message_id)
      k+=1
      time.sleep(15)
      print(bot.copyMessage(chat_id,from_chat,2).message_id)
      print(bot2.sendMessage(chat_id,"Jai Shree Ram🚩").message_id)
      print(bot.copyMessage(chat_id,from_chat,3).message_id)
    except Exception as ee:
      print("Andar Ka Error",ee)
      time.sleep(30)
