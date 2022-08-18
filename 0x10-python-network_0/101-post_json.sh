#!/bin/bash                                                                                      
# Display body if status number eq 200                                                           
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
