#!/usr/bin/python3
def safe_print_integer(value):
    try: #If value is an integer
        print("{:d}".format(value))
        return True
    except: #Value it is not an integer
        return False
