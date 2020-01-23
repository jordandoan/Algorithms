#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  dp = [1] + [0]*(n)
  cookies = [1,2,3]
  for i in range(n + 1):
    for cookie in cookies:
      if dp[i - cookie]:
        dp[i] += dp[i - cookie]
  return dp[-1]
  # def bt(n):
  #   if n < 0:
  #     return 0
  #   if n == 0:
  #     return 1
  #   total = 0
  #   for i in range(1,4):
  #     total += (bt(n-i))
  #   return total
  # return bt(n)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')