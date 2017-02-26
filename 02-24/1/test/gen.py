from random import randint

cases = 100

print cases
for i in range(cases):
  start = randint(1, 1000)
  finish = start
  while (start == finish):
    finish = randint(1, 1000)
  print str(start) + ' ' + str(finish)
