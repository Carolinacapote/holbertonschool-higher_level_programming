#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_number = number % 10
if (number < 0):
    last_number = (number * -1) % 10 * -1
str1 = " and is less than 6 and not 0"
str2 = " and is greater than 5"
if (last_number < 6 and last_number != 0):
    print("Last digit of {} is {}".format(number, last_number) + str1)
elif (last_number > 5):
    print("Last digit of {} is {}".format(number, last_number) + str2)
else:
    print("Last digit of {} is {} and is 0".format(number, last_number))
