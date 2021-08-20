#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8).
'''


if __name__ == "__main__":
    from sys import argv
    from urllib import request, error, parse

    try:
        with request.urlopen(argv[1]) as response:
            print('Index')

    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
