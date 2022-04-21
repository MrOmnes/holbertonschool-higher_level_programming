#!/bin/bash
# Curl and grep content length
curl -sI -X OPTIONS "$1" | grep Allow | cut -d " " -f2
