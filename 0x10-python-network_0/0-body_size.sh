#!/bin/bash
# Display size of body in bytes
if (("$#" == 1))
then
	curl -s "$1" -w '%{size_download}'
fi
