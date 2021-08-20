#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8).
'''


if __name__ == "__main__":
    from sys import argv
    from urllib import request, error, parse

    new_request = request.Request(argv[1])

    try:
        request.urlopen(new_request)
        print('Index')

    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
