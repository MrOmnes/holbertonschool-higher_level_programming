#!/bin/bash                                                                                      
# Display body if status number eq 200
curl -s -X POST -F 'email=test@gmail.com' -F 'subject=I will always be here for PLD' "$1"
