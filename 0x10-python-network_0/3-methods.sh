#!/bin/bash
# Taking in URL, displays all the methods accepted.
curl -sI "$1" | grep 'Allow:' | cut -f2- -d' '
