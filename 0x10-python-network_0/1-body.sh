#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
STATUS_CODE=$(curl -sI "$1" | head -n 1 | cut -d ' ' -f2)
if [[ $STATUS_CODE == 200 ]]
then
	curl -s "$1"
fi
