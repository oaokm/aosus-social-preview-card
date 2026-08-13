from config import config
from style import style
import os, base64

from utils import (
    getUserProfileImageUrlPath
)

class htmlBody:
    def __init__(self, htmlTemplate:str, data:dict):
        self.ok   = True
        self.htmlTemplate = htmlTemplate
        self.data = data

        self.htmlTemplatePath = os.path.join('htmlTemplate', self.htmlTemplate)
        if not os.path.exists(self.htmlTemplatePath):
            self.ok = False
            print(f"[htmlBody]: `{self.htmlTemplatePath}` is not exists!")

        
    def _setCard(self):
        cardHeader = f""" 
        <!-- الرأس: الشعار في اليمين -->
        <div class="card-header">
            <div class="badge">{self.data.get('tag')}</div>
            <div class="divider"></div>
            <div class="user-info">
                <span class="username">{self.data.get('username')}</span>
                <img class="avatar" src="https://{config.domainBase}{self.data.get('profileImageUrlPath')}">
            </div>
            <div class="divider"></div>
            <img src="https://cdn-cf-discourse.aosus.org/original/2X/8/85cdc7c9b017edb30f0afd89232bc4ec24fc933e.svg" alt="Logo" class="logo">
        </div>"""
        
        cardBody = f"""
        <div class="card-body">
            <h1>{self.data.get('title')}</h1>
            <p>{self.data.get('text')} ...</p>
        </div>"""

        cardFooter = """
        <!-- التذييل -->
        <div class="card-footer">
            <div class="footer-text">تقني &middot; رائد &middot; عربي</div>
            <div class="footer-link"> aosus.org </div>
        </div>
        
        <!-- صورة الزخرفة (توضع هنا كآخر عنصر) -->
        <img src="./images/x.png" class="decoration-image">
        """

        cardBase   = f"""<div class="card">\n{cardHeader}\n{cardBody}\n{cardFooter}</div>"""
        return cardBase
    
    def setHTML(self):
        # ./{os.path.join(self.htmlTemplatePath, 'style.css')}
        htmlHead     = f"""<head> <link rel="stylesheet" href="/home/superoaokm/Codes/aosus-social-preview-card/aosusSocialCard/htmlTemplate/aosusTest/style.css"> </head>"""
        #htmlHead     = f"""<head> \n<style> \n{style(htmlTemplate=self.htmlTemplate).setCssFile(getStyle=True)} \n</style>\n</head>"""
        htmlBody     = f"""<body>{self._setCard()}</body>"""
        htmlFullBody = f"""<!DOCTYPE html>\n<html lang="ar">\n{htmlHead}\n{htmlBody}</html>"""

        htmlPath = os.path.join(self.htmlTemplatePath, 'test.html')
        with open(htmlPath, 'w+', encoding='utf-8') as file:
            if file.writable():
                file.write(htmlFullBody)
                file.close()
                return True
            else:
                print(f'[htmlBody.setHTML]: opss! can not write on `{htmlPath}`')
                return False
            

if __name__ == '__main__':
    username = 'islamux'
    print(htmlBody(htmlTemplate='aosusTest', data={
        'username': username, 
        'profileImageUrlPath': getUserProfileImageUrlPath(username),
        'title': "تطبيق ويب من سيربح المليون مبني على كتاب بصائر لمكافحة الإلحاد",
        'text': "السلام عليكم ورحمة الله وبركاته برمجت تطبيق ويب من سيربح المليون مصدرة هو كتاب الدكتور هيثم طلعت بصائر والذي قال عنه انه مشروع العمر لمكافحة الافكار الالحادية المنتشرة",
        'tag': " | ".join(['برمجة' , 'المشاريع', "البرمجة"])
        }).setHTML())



