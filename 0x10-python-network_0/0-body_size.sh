#!/bin/bash
# It takes in a URL, sends a request to that URL, and displays the size of the body in bytes of the response
curl -s "$1" | wc -c
