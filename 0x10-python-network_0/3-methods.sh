#!/bin/bash
#Display the body of the Response
curl -Is "$1" | grep "Allow: " | cut -d ' ' -f 2-
