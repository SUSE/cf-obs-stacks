#!/bin/bash
set -e

for token in ${OBS_TOKENS}
do
     curl -s -H "Authorization: Token ${token}" -X POST 'https://api.opensuse.org/trigger/runservice'
done
