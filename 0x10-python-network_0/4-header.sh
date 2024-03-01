#!/bin/bash
# Taking in URL, adding header variable, and displays "Hello School!".
curl -s -H "X-School-User-Id":98 "$1"
