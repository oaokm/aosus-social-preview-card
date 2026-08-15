from config import config
from style import style
import os, base64


class htmlBody:
    """
    htmlBody: the object that responsible to deal with HTML 

    args:
        - data(dict): a value resulting from an extraction process (aosusExtracter) from an article page for aosus discourse

    variables:
        - ok(bool): if it is "True", this means that nothing is hindering the object's operation.
        - tag(str): a value from `data` represents an article's tags
        - tagsColor(str): a hexadecimal color value represents the article's first tag color.
    """
    def __init__(self, data:dict):
        self.ok   = True
        self.data = data
        self.tag = self.data.get('tag')
        
        if self.tag:
            color = self.tag.split(' | ')[0]
            self.tagsColor = config.tagsColors.get(color, '#1d8337')
        else:
            self.tagsColor = '#1d8337'

        self.htmlTemplatePath = './htmlTemplate'


    def _setCard(self):
        """
        _setCard: a function responsible to creat a social preview card as HTML syntex
        """
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
        
        <!-- صورة الزخرفة (غلى يمين الكرت) -->
        <img src="./images/x.png" class="decoration-image">

        <!-- صورة الزخرفة (على يسار الكرت) -->
        <img src="./images/left-side.png" class="decoration-image-left">

        <!-- صورة الزخرفة (العلوية) -->
        <img src="./images/top-side.png" class="decoration-image-top">
        """

        cardBase   = f"""<div class="card">\n{cardHeader}\n{cardBody}\n{cardFooter}</div>"""
        return cardBase
    
    def setHTML(self):
        """
        setHTML: the function responsible to create HTML file/generate a social preview card ;)
        """
        s = style(_withStyleTag=True)
        htmlHead     = f"""<head>\n\t<meta charset="UTF-8">\n\t{s.fontFace} \n\t<link rel="stylesheet" href="data:text/css;base64,{base64.b64encode(s.setCssSyntax(badgesColor=self.tagsColor)).decode('utf-8')}"> \n</head>"""
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
            


