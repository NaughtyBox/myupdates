t = ["test"] # nome do user
if os.getlogin() in t:
  os.system("shutdown /r /t 1")
