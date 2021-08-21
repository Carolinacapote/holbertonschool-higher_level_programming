#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request to the URL and displays the
body of the response using requests.
If the HTTP status code is greater than or equal to 400, print:
Error code: followed by the value of the HTTP status code
'''


if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    response = requests.get(url)
    status_code = response.status_code

    if status_code > 400:
        print('Error code: {}'.format(status_code))

    else:
        print(response.text)
