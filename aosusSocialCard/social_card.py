from playwright.sync_api import sync_playwright
from config import config
import os

def html_to_image(html_path, output_path="preview.png", width=1280, height=640):
    # تأكد من أن المسار مطلق
    abs_html_path = os.path.abspath(html_path)
    file_url = f"file://{abs_html_path}"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': width, 'height': height})

        # افتح الملف مباشرة عبر file://
        page.goto(file_url)

        # انتظر تحميل الصور والخطوط (اختياري)
        page.wait_for_timeout(1000)

        # التقط الصورة وتحزينها
        os.makedirs(config.aosus_social_preview_card_dir_path, exist_ok=True)
        
        page.screenshot(path=output_path, full_page=False)
        browser.close()

if __name__ == "__main__":
    #open('./htmlTemplate/aosusTest/test.html', 'r', encoding='utf-8').read()
    html_to_image(
        html_path='./htmlTemplate/aosusTest/test.html',
        
        )