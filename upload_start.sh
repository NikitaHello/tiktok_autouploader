#!/bin/bash
touch Logging/app.log
echo "Starting manager.py" > Logging/log.txt
source venv/bin/activate
python manager.py