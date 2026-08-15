from fastapi.responses import FileResponse, HTMLResponse
from fastapi import FastAPI, HTTPException
from config import config
from pathlib import Path
import os

from config import config
from utils import (
    extractArticleID
)

os.chdir(os.path.dirname(os.path.realpath(__file__)))


BASE_DIR = Path(config.aosus_social_preview_card_dir_path)  


# تأكد من وجود المجلد
if not BASE_DIR.exists():
    raise Exception(f"{BASE_DIR} not exist!")

app = FastAPI(title="Aosus-Social-Preview-Card")

def is_path_allowed(requested_path: str) -> Path:
    """
    تحويل المسار النسبي إلى مسار مطلق مع التحقق من أنه داخل BASE_DIR.
    """
    # نمنع محاولات الخروج باستخدام ..
    clean_path = Path(requested_path)
    # نتأكد من أن المسار ليس مطلقاً (نسبي) لتجنب اختراق الأمان
    if clean_path.is_absolute():
        raise HTTPException(status_code=400, detail="the path was wrong")
    
    full_path = (BASE_DIR / clean_path).resolve()
    # التحقق من أن المسار الناتج يقع تحت BASE_DIR
    if not str(full_path).startswith(str(BASE_DIR.resolve())):
        raise HTTPException(status_code=403, detail="غير مسموح بالوصول إلى هذا الموقع")
    return full_path



@app.get("/{url:path}")
async def get_file(url: str):
    """
    يقرأ ويعيد محتوى الملف (صور، نصوص، PDF، إلخ) كاستجابة مناسبة.
    لتنزيل الملف استخدم /download بدلاً من ذلك.
    """
    try:
        id = extractArticleID(url)
        filename = id+'.png'
        full = is_path_allowed(filename)
        if not full.is_file():
            raise HTTPException(status_code=404, detail="file not exists")
        return FileResponse(full)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# لتشغيل الخادم (يمكنك تنفيذ الملف مباشرة)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=config.tcpPort)
