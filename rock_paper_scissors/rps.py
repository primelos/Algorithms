#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  
  def crt_arr(lis, num):
    if len(lis) == n:
      return [lis]
    else:
      return crt_arr(lis + ['rock'], num) + crt_arr(lis + ['paper'], num) + crt_arr(lis + ['scissors'], num)
  return crt_arr([], n)

rock_paper_scissors(3)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')