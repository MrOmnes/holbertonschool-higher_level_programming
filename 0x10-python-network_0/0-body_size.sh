#!/bin/bash
# Display size of body in bytes
curl -s "$1" -w '%{size_download}\n'
