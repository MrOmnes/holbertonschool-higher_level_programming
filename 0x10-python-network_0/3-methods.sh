#!/bin/bash
# Curl and grep content length
curl -X OPTIONS $1 | grep Allow | cut -d " " -f2
