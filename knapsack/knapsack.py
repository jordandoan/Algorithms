#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):
    # items[i][1] = weight
    # items[i][2] = value
    def bt(items, current, capacity):
        if capacity < 0:
            return {'Value': -1}
        if not items or capacity == 0:
            return current
        new_current = current
        for i, item in enumerate(items):
          new_current = max(
            [new_current, bt(items[0:i] + items[i+1:], {'Value': current['Value'] + item[2], 'Chosen': current['Chosen'] + [item[0]]}, capacity-item[1])],
            key=lambda obj: obj["Value"]
          )
        return new_current
    opt_items = bt(items, {'Value': 0, 'Chosen': []}, capacity)
    return opt_items


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
