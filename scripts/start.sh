#!/bin/bash

echo "Starting Telegram bot..."

source .env
source venv/bin/activate

python bot/main.py &
echo $! > bot.pid

echo "Bot started"
