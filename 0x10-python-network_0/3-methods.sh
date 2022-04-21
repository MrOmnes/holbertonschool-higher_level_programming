#!/bin/bash
# Curl and grep content length
curl -X OPTIONS "$1" -si | grep Allow | cut -d " " -f 2-
