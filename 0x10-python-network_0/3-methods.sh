#!/bin/bash                                                                                      
# Display body if status number eq 200                                                           
curl -i -s -L  "$1" -X OPTIONS | grep -E "Allow:" | cut -d ' ' -f 2-
