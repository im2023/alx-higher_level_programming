#!/bin/bash
# Displayes size of body of response.
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f 2
