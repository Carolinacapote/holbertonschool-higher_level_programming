#!/usr/bin/python3
'''
Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)
'''


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv

    url = argv[1]
    parameters = {
        'email': argv[2]
    }

    query_str = urllib.parse.urlencode(parameters)
    data = query_str.encode()

    with urllib.request.urlopen(url, data) as response:
        response_text = response.read().decode('utf-8')

    print(response_text)
