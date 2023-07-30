#!/usr/bin/env python

# Simple tool to send a text message to nick via AWS

import sys
import requests


def send_message(message):
    url = 'https://m5s2b31841.execute-api.us-east-2.amazonaws.com/prod/'
    
    try:
        response = requests.get(url, params={'message': message})
        response.raise_for_status()
    except Exception as e:
        # If the request fails, exit with a status code of 1
        print(e)
        sys.exit(1)

    # If the request is sent successfully, exit with a status code of 0
    sys.exit(0)


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Usage: python script.py <message>')
        sys.exit(1)

    message = sys.argv[1]

    send_message(message)
