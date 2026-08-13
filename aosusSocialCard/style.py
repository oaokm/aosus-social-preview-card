from config import config
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

    def setCssFile(self):
        if self.ok:
            baseCssFileParh = config.baseCss
            baseCssData     = None
            cssTempFilePath = os.path.join(self.htmlTemplatePath, 'style.css')
            cssTempData     = None
    

            with open(baseCssFileParh, 'r', encoding='utf-8') as file:
                baseCssData = file.read()
                file.close()

            
            with open(cssTempFilePath, 'w+', encoding='utf-8') as file:
                if file.writable():
                    file.write(f"{self.fontFace}\n{baseCssData}")
                    file.close()
                    return True
                else:
                    print(f'[style.setCssFile]: opss! can not write on `{cssTempFilePath}`')
                    return False



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
            return f"""<style>{fontFace}</style>"""
        
        return fontFace

if __name__ == '__main__':
    print(style(htmlTemplate='aosusTest').setCssFile())