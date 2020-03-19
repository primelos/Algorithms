#!/usr/bin/python

import argparse

def find_max_profit(prices):
  profit = prices [1] - prices[0]
  # cost = prices[0]
  
  for i in prices[1:]:
    if(i - prices[0]) > profit:
      profit = i - prices[0]
    
  
  return profit

print(find_max_profit([100, 90, 80, 50, 20, 10]))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))