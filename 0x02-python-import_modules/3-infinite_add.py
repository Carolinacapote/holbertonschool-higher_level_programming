#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    numbers = len(argv)
    if numbers == 0:
        print(numbers)
    else:
        sum = 0
        for i in range(1, numbers):
            sum += int(argv[i])
        print("{}".format(sum))
