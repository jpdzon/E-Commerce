#!/bin/bash

# Create MongoDB data directory if it doesn't exist
mkdir -p /home/runner/data/db

# Start MongoDB in background
mongod --dbpath /home/runner/data/db --bind_ip 127.0.0.1 --port 27017 --fork --logpath /home/runner/data/mongod.log

# Wait for MongoDB to be ready
echo "Waiting for MongoDB to start..."
sleep 3

# Start Flask app
python main.py
