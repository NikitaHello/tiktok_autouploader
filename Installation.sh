#!/bin/bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd tiktok_uploader/tiktok-signature/
npm i