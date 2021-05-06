#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_one = set_1 - set_2
    set_two = set_2 - set_1
    return (set_one | set_two)
