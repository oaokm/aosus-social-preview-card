from playwright.sync_api import sync_playwright
from config import config
import os

def html_to_image(html_path, output_path, width=1280, height=640):
    """
    html_to_image: the function that responsible to convert html syntex to png image

    args:
        - html_path(str): file path for html code
        - output_path(str):
        - width(int): the dimensions of the generated image are represented in terms of width. default is 1280 px
        - height(int): the dimensions of the generated image are represented in terms of height. default is 640 px
    """
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
