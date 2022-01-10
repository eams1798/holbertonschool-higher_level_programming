#!/bin/bash
#takes a url as an arg and send a GET request 
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" $1
