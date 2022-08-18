#!/bin/bash
# Display size of body in bytes
curl -sI "$1" | awk '/Content-Length/{print $2}'
