#!/bin/bash
sleep 1
cd $*
while read line; do
    export $line
done < .env
pm2 --name $PM2NAME start node_modules/node-red/red.js --node-args="--max-old-space-size=384" --restart-delay 10000 -- -s ./settings.js -u ./

