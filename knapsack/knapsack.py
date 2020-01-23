#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

# # Brute Force
# def knapsack_solver(items, capacity):
#     # items[i][1] = weight
#     # items[i][2] = value
#     def bt(items, current, capacity):
#         if capacity < 0:
#             return {'Value': -1}
#         if not items or capacity == 0:
#             return current
#         new_current = current
#         for i, item in enumerate(items):
#             next_iter = {'Value': current['Value'] + item[2], 'Chosen': current['Chosen'] + [item[0]]}
#             new_current = max(
#                 [new_current, bt(items[0:i] + items[i+1:], next_iter, capacity-item[1])],
#                 key=lambda obj: obj["Value"]
#             )
#         return new_current
#     return bt(items, {'Value': 0, 'Chosen': []}, capacity)

# DP attempt
def knapsack_solver(items, capacity):
    # items[i][1] = weight
    # items[i][2] = value
    dp = [[0]*(capacity+ 1) for i in items]
    for col in range(1,capacity+1):
        for row in range(len(items)):
            if col - items[row][1] < 0:
                # if item is too heavy, it's the same result as row above it
                dp[row][col] = dp[row-1][col]
            else:
                if row == 0:
                    # edge case, since we do row-1
                    dp[row][col] = max(items[row][2], dp[row][col-1])
                else:
                    # compare current val + val without that item vs val of previous row
                    dp[row][col] = max(items[row][2] + dp[row-1][col-items[row][1]], dp[row-1][col])
    # for row in dp:
    #     print(row)
    return dp[-1][-1]
if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
arr = [
    [1, 2, 4],
    [2, 4, 10],
    [3, 1, 1],
    [4, 3, 7],
    [5, 5, 2]
]
print(knapsack_solver(arr, 5))