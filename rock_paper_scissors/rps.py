#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  
  def generate(l, num):
    if len(l) == n:
      return [l]
    else:
      return generate(l + ['rock'], num) + generate(l + ['paper'], num) + generate(l + ['scissors'], num)
  return generate([], n)

rock_paper_scissors(3)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')