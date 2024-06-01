#!/bin/bash
sudo apt install python3
sudo apt install npm
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd tiktok_uploader/tiktok-signature/
npm i