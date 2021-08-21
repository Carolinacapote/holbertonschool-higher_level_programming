#!/usr/bin/python3
'''
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
'''


if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': ''}

    if len(argv) == 2:
        data['q'] = argv[1]

    response = requests.post(url, data)

    try:
        valid_js = response.json()
        if len(valid_js) is not 0:
            print('[{}] {}'.format(valid_js.get('id'), valid_js.get('name')))
        else:
            print('No result')

    except ValueError:
        print('Not a valid JSON')
