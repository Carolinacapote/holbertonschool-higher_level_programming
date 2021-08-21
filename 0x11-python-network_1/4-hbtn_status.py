#!/usr/bin/python3
'''
Python script that fetches https://intranet.hbtn.io/status with requests
'''


if __name__ == "__main__":
    import requests

    url = 'https://intranet.hbtn.io/status'
    new_request = requests.get(url)

    print('Body response:')
    print('\t- type: {}'.format(type(new_request.text)))
    print('\t- content: {}'.format(new_request.text))
