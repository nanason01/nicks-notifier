#!/usr/bin/env python

# Simple tool to send a text message to nick via AWS

import sys
import requests
import json


def send_message(url, message):
    headers = {'Content-Type': 'application/json'}
    payload = {'message': message}

    try:
        response = requests.post(url, headers=headers,
                                 data=json.dumps(payload))
        response.raise_for_status()
    except Exception as e:
        # If the request fails, exit with a status code of 1
        print(e)
        sys.exit(1)

    # If the request is sent successfully, exit with a status code of 0
    sys.exit(0)


if __name__ == '__main__':
    url = 'https://t7n4heq5w4.execute-api.us-east-1.amazonaws.com/prod'

    if len(sys.argv) < 2:
        print('Usage: python script.py <message>')
        sys.exit(1)

    message = sys.argv[1]

    send_message(url, message)
