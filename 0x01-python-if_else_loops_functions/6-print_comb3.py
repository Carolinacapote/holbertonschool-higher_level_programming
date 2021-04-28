#!/usr/bin/python3
for left_digit in range(9):
    right_digit = left_digit + 1
    while right_digit < 10:
        if (left_digit != 8):
            print("{}{},".format(left_digit, right_digit), end=" ")
        else:
            print("{}{}".format(left_digit, right_digit))
        right_digit += 1
