#!/bin/bash
PID_FILE="app.pid"

if [ -f "$PID_FILE" ] && kill -0 $(cat "$PID_FILE") 2>/dev/null; then
    echo "✅ the application is running (PID: $(cat $PID_FILE))"
else
    echo "❌ the application was suspended"
fi