#!/bin/bash
#script takes in a URL, sends a request to that URL,
curl -sI "$1" | grep -i 'content-length' | awk '{print $2}'
