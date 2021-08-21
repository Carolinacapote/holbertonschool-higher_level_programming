#!/usr/bin/python3
'''
Python script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id.
 Basic Authentication with a personal access token as password to access.
'''


if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv

    url = 'https://api.github.com/user'
    user_name = argv[1]
    passwd = argv[2]

    response = requests.get(url, auth=HTTPBasicAuth(user_name, passwd))
    user_id = response.json.get('id')

    print(user_id)
