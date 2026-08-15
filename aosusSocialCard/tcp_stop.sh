#!/bin/bash
PID_FILE="app.pid"

if [ ! -f "$PID_FILE" ]; then
    echo "❌ PID file not found (Service not running?)"
    exit 1
fi

PID=$(cat "$PID_FILE")
if kill -0 "$PID" 2>/dev/null; then
    echo "🛑 application is being suspended (PID: $PID)..."
    kill "$PID"
    rm "$PID_FILE"
    echo "✅ suspended was successful"
else
    echo "⚠️ The process is not working; the old PID file has been deleted."
    rm "$PID_FILE"
fi