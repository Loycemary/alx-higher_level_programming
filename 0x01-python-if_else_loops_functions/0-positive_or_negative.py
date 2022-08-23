#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if num > 0:
    print("{:d} is positive".format(number))
elif num == 0:
    print("{:d} is zero".format(number))
elif num < 0:
    print("{:d} is negative".format(number))
