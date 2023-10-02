#!/usr/bin/python3
import sys
import math

def print(*objects, sep=' ', end='\n'):
  text = sep.join(map(str, objects))
  sys.stdout.write(f'{text}{end}')

def input():
  return sys.stdin.readline().rstrip('\r\n')

def _main() -> None:
  n = int(input())
  for i in range(n):
    a, b, c = map(int, input().split(" "))
    minDiv = math.ceil(a / c) * c
    maxDiv = math.floor(b / c) * c

    divSum = 0

    # if one of them is off-limits both of them are
    if minDiv > b or maxDiv < a:
      pass
    elif minDiv == maxDiv:
      divSum = c
    else:
      divSum = ((maxDiv - minDiv)//c + 1) * (minDiv + maxDiv) // 2

    allSum = (b-a+1)*(b+a)//2

    print(allSum - divSum)


if __name__ == '__main__':
  _main()
