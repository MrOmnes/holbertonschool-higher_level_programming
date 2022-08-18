#!/bin/bash                                                                                      
# Display body if status number eq 200
curl -s -X POST -F 'subject=I will always be here for PLD' -F 'email=test@gmail.com' "$1"