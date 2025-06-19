#!/bin/bash

# Jack Dalton's Portfolio Development Server Starter
# This script starts a local development server for your Jekyll website

echo "🚀 Starting Jack Dalton's Portfolio Development Server..."
echo

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    python3 local-server.py
elif command -v python &> /dev/null; then
    python local-server.py
else
    echo "❌ Python is not installed or not found in PATH"
    echo "Please install Python 3 to run the development server"
    exit 1
fi
