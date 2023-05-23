#!/bin/bash

be_ip=127.0.0.1
be_url=http://$be_ip/get_data
no_bot=Bottle-wl
yes_bot=Bottle-l
poll_freq=1
timeout=10

while true; do
  r="$(curl -s $be_url)"
  if echo "$r" | grep -q $no_bot; then
    ./red.py
    i=0
  elif echo "$r" | grep -q $yes_bot; then
    ./green.py
    i=0
  else
    ((i++))
    if [[ $i -gt $timeout ]]; then
      ./off.py
    fi
  fi
done

