#!/usr/bin/python3
'''
Python script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id.
 Basic Authentication with a personal access token as password to access.
'''
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user_name = argv[1]
    passwd = argv[2]
    response = requests.get(url, auth=HTTPBasicAuth(user_name, passwd))

    if response.status_id is 200:
        user_id = response.json.get('id')
    else:
        user_id = None

    print(user_id)
