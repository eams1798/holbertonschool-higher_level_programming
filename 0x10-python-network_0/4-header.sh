#!/bin/bash
#takes a url as an arg and send a GET request 
curl -sX GET -H "X-School-User-Id: 98" $1
