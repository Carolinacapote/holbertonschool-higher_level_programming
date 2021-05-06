#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic_copy = {}
    for key in sorted(a_dictionary):
        dic_copy[key] = a_dictionary[key]
        print("{}: {}".format(key, dic_copy[key]))
