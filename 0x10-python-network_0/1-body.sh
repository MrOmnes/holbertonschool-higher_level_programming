#!/bin/bash
# Display body if status number eq 200
curl -sI "$1" -eq 200
