#!/bin/bash

for token in ${OBS_TOKENS}
do
     curl -H "Authorization: Token ${token}" -X POST 'https://api.opensuse.org/trigger/runservice'
done
