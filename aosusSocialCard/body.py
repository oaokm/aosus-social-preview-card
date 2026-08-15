from config import config
from style import style
import os, base64
from aosus_extracter import aosusExtracter
from utils import (
    getUserProfileImageUrlPath
)

class htmlBody:
    def __init__(self, htmlTemplate:str, data:dict):
        self.ok   = True
        self.htmlTemplate = htmlTemplate
        self.data = data
        self.tag = self.data.get('tag')
        
        if self.tag:
            color = self.tag.split(' | ')[0]
            print(color)
            self.tagsColor = config.tagsColors.get(color, '#1d8337')
            print(self.tagsColor)
        else:
            self.tagsColor = '#1d8337'

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

        <!-- صورة الزخرفة (توضع هنا كآخر عنصر) -->
        <img src="./images/left-side.png" class="decoration-image-left">

        <!-- صورة الزخرفة (توضع هنا كآخر عنصر) -->
        <img src="./images/top-side.png" class="decoration-image-top">
        """

        cardBase   = f"""<div class="card">\n{cardHeader}\n{cardBody}\n{cardFooter}</div>"""
        return cardBase
    
    def setHTML(self):
        s = style(htmlTemplate=self.htmlTemplate)
        htmlHead     = f"""<head>\n\t<meta charset="UTF-8">\n\t{s._setFontFace(withStyleTag=True)} \n\t<link rel="stylesheet" href="data:text/css;base64,{base64.b64encode(s.setCssFile(justGetStyle=True, badgesColor=self.tagsColor)).decode('utf-8')}"> \n</head>"""
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
    url = 'https://discourse.aosus.org/t/topic/3229'

    print(htmlBody(htmlTemplate='aosusTest', data=aosusExtracter(url)._extractArtcleData()).setHTML())
    


