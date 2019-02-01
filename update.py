def test():
  print('this is a test')
  with open('testupdator.txt', 'w') as fp:
    fp.write('success')

test()
