#!/bin/bash

echo "Writing configuration..."
python configurator.py
echo "Initializing elasticsearch status index"
elastalert-create-index --index elastalert_status --old-index ""
echo "Starting elastalert..."
elastalert --verbose
