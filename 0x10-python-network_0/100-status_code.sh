#!/bin/bash                                                                                      
# Display body if status number eq 200                                                           
curl -i -s -L  "$1"| grep -E "HTTP/" | cut -d ' ' -f 2 | tr -d '\n'
