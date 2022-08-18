#!/bin/bash                                                                                      
# Display body if status number eq 200                                                           
curl -s -L "$1" -X PUT -d 'user_id=98' 0.0.0.0:5000/catch_me
