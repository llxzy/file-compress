#!/bin/bash
crontab -l > convert_cron
echo "0 0 1 * * /usr/bin/python3 $(pwd)/main.py /var/log" >> convert_cron
crontab convert_cron
rm convert_cron
