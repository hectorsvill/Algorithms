#!/usr/bin/python

import argparse

def find_max_profit(prices):
    prices_len = len(prices)
    current_min_price_so_far = 0
    find_max_profit = 0

    i = 0
    while (i < prices_len):

        p = 0
        while(p < prices_len):
            # print(abs(prices[i] - prices[p]))
            if current_min_price_so_far < prices[i] - prices[p]:
                current_min_price_so_far = prices[i] - prices[p]
            p += 1

        i += 1

    return current_min_price_so_far

l1 = [100, 90, 80, 50, 20, 10] # -10
l2 = [10, 7, 5, 8, 11, 9] # 6
x = find_max_profit(l2)
print(x)

#
# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()
#
#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
