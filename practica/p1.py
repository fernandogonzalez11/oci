#!/usr/bin/python3
import sys

def print(*objects, sep=' ', end='\n'):
    text = sep.join(map(str, objects))
    sys.stdout.write(f'{text}{end}')

def input():
  return sys.stdin.readline().rstrip('\r\n')

def _main() -> None:
  # 
  pass

if __name__ == '__main__':
  _main()
