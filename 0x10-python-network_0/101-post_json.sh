#!/bin/bash
# Taking filename and URL, and posting contents of file.
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
