#!/bin/bash

echo "Writing configuration..."
python configurator.py
echo "Initializing elasticsearch status index"
elastalert-create-index --index elastalert_status <<< $'\n'
echo "Starting elastalert..."
elastalert --verbose
