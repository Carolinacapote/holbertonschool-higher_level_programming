#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
     if a_dictionary == None:
          return None
     a_dictionary.update({key : value})
     return (a_dictionary)
