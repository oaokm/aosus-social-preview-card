#!/bin/bash
# اسم الملف الذي يحتوي على الكود (عدله حسب اسم ملفك)
APP_FILE="tcp.py"
# اسم ملف PID لتتبع العملية
PID_FILE="app.pid"

LOGPATH="./logs/tcp_app.log"

# التحقق من وجود مجلد السجلات log

if [ ! -d "logs" ]; then
    echo "[tcp_start] Create logs dir."
    mkdir logs
fi


# التحقق إذا كانت الخدمة تعمل مسبقاً
if [ -f "$PID_FILE" ] && kill -0 $(cat "$PID_FILE") 2>/dev/null; then
    echo "⚠️  the application is already running  (PID: $(cat $PID_FILE))"
    exit 1
fi

echo "🚀 The TCP/IP application is running in the background...."
# تشغيل uvicorn مع إعادة التوجيه إلى ملف سجل (log)
nohup /usr/aosusSocialPreviewCardVenv/bin/python ./$APP_FILE > $LOGPATH 2>&1 &

# حفظ معرف العملية (PID)
echo $! > "$PID_FILE"
echo "✅ running successful (PID: $(cat $PID_FILE))"
echo "📋 to see log -> tail -f $LOGPATH"