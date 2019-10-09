#!/usr/bin/python

import argparse

def find_max_profit(prices):
    print("here")
    i = 0
    current_min_price_so_far = prices[0]
    find_max_profit = 0

    while (i < len(prices)):
        print(prices[i])
        i += 1

    return -1

l = [10, 7, 5, 8, 11, 9]
find_max_profit(l)


#
# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()
#
#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
