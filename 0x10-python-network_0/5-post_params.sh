#!/bin/bash
#takes in a url and sends a POST request and displays response"
curl -s "$1" -d "email=test@gmail.com&subject=\
	I%20will%20always%20be%20here%20for%20PLD"
