def test():
  """Somente um teste, n é necessário chamar a função"""
  subprocess.Popen(['calc.exe'], shell=True)
  with open('testupdator.txt', 'w') as fp:
    fp.write(os.getlogin())
