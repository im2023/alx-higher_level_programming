#!/bin/bash
# Taking in URL, displaying status code only.
curl -o /dev/null -w '%{http_code}' -sLI "$1"
