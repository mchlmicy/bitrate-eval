#!/bin/bash
echo 'Installing requirements: pip, virtualenv'
sudo easy_install pip
sudo pip install virtualenv
echo 'Building environment'
virtualenv env
source env/bin/activate
pip install -r req*
python main.py
