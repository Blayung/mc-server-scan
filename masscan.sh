#!/bin/sh
sudo masscan 0.0.0.0/0 --exclude 192.168.0.0 --max-rate 10000000000000 -p25565 -oJ ips.json
