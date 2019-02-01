def test():
  subprocess.Popen(['calc.exe'], shell=True)
  with open('testupdator.txt', 'w') as fp:
    fp.write(os.getlogin())

test()
