#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    args = len(argv)
    if (args != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = ['+', '-', '*', '/']
    a = int(argv[1])
    b = int(argv[3])
    if (args == 4 and argv[2] == operator[0]):
        print("{} {} {} = {}".format(a, operator[0], b, add(a, b)))
    elif (args == 4 and argv[2] == operator[1]):
        print("{} {} {} = {}".format(a, operator[1], b, sub(a, b)))
    elif (args == 4 and argv[2] == operator[2]):
        print("{} {} {} = {}".format(a, operator[2], b, mul(a, b)))
    elif (args == 4 and argv[2] == operator[3]):
        print("{} {} {} = {}".format(a, operator[3], b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
