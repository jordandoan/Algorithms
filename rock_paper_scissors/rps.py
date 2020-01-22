#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  ans = []
  choices = ['rock', 'paper', 'scissors']
  def bt(curr, n):
    if not n:
      ans.append(curr)
      return ans
    for choice in choices:
      bt(curr + [choice], n-1)
    return ans
  return bt([], n)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')