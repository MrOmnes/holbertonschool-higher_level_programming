#!/bin/bash                                                                                      
# Display body if status number eq 200                                                           
curl -o /dev/null -s -L -w "%{http_code}" "$1"
