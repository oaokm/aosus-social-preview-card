from config import config
from io import BytesIO
import base64
import os

class style:
    def __init__(self, htmlTemplate:str, _withStyleTag=False):
        self.ok               = True
        self.fontFace         = self._setFontFace(_withStyleTag)
        self.htmlTemplatePath = os.path.join('htmlTemplate', htmlTemplate)
        if not os.path.exists(self.htmlTemplatePath):
            self.ok = False
            print(f"[style]: `{self.htmlTemplatePath}` is not exists!")

    
    def _font_to_base64(self, file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")


    def setCssFile(self, getStyle=False, justGetStyle=False, badgesColor='#1d8337'):
        if self.ok:
            baseCssFileParh = config.baseCss
            baseCssData     = None
            cssTempFilePath = os.path.join(self.htmlTemplatePath, 'style.css')
            cssTempData     = None
    
            badgeSet =  f"""
                display: inline-block;
                background-color: {badgesColor};
                color: #FFF;
                padding: 4px 12px;
                border-radius: 40px;
                
                font-size: 18px;
                font-weight: 700;
                font-family: 'Alyamama';
                
                white-space: nowrap;
                border: 1px solid #374151;

                direction: rtl;
                """

            with open(baseCssFileParh, 'r', encoding='utf-8') as file:
                baseCssData = file.read() + f'.badge{{ {badgeSet} }}'
                file.close()

            if not getStyle:
                with open(cssTempFilePath, 'w+', encoding='utf-8') as file:
                    if file.writable():
                        file.write(f"{self.fontFace}\n{baseCssData}\n.badge{{ {badgeSet} }}")
                        file.close()
                        if justGetStyle:
                            return baseCssData.encode('utf-8')
                        return True
                    else:
                        print(f'[style.setCssFile]: opss! can not write on `{cssTempFilePath}`')
                        return False
            
            return BytesIO(f"{self.fontFace}\n{baseCssData}".encode('utf-8'))


    def _setFontFace(self, withStyleTag=False):
        for filename, weight in config.font_weights.items():
            file_path = os.path.join(config.fontsPath, filename)
            if not os.path.exists(file_path):
                continue
            
            # تحويل الملف إلى Base64
            b64_string = self._font_to_base64(file_path)
            # تحديد نوع الخط (عادة TrueType)
            mime_type = "font/ttf"
            
            # إنشاء تعريف @font-face
            fontFace = f"""@font-face {{
                    font-family: 'Alyamama';
                    src: url('data:{mime_type};charset=utf-8;base64,{b64_string}') format('truetype');
                    font-weight: {weight};
                    font-style: normal;
                    font-display: swap;
                }}"""
        if withStyleTag:
            return f"""<style>\n\t{fontFace}\n</style>"""
        
        return fontFace

if __name__ == '__main__':
    print(style(htmlTemplate='aosusTest').setCssFile())