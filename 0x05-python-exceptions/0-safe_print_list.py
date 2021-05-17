#!/usr/bin/python3
"""Function that prints x elements of a list.

Return: Number of elements printed
x: Number of elements to be printed
"""
def safe_print_list(my_list=[], x=0):
    printed_elements = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            printed_elements += 1
        except:
            pass

    print()
    return (printed_elements)
