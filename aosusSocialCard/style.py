from config import config
import base64
import os

class style:
    """
    style: the object that responsible to deal with CSS 

    args:
        - _withStyleTag(bool): get CSS syntax with <style>. default is `false`

    variables:
        - ok(bool): if it is "True", this means that nothing is hindering the object's operation.
        - fontFace(str): the value of CSS @font-face syntax
    """
    def __init__(self, _withStyleTag=False):
        self.ok               = True
        self.fontFace         = self._setFontFace(_withStyleTag)


    def _fontToBase64(self, file_path):
        """
        _fontToBase64
        """
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")


    def setCssSyntax(self, badgesColor='#1d8337'):
        """
        setCssSyntax: the function that responsible to create/set full css syntex

        args:
            - badgesColor(str): a hexadecimal color value represents the article's first tag color. default is `#1d8337`
        """
        if self.ok:
            baseCssFileParh = config.baseCss
    
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

            return baseCssData.encode('utf-8')


    def _setFontFace(self, withStyleTag=False):
        """
        _setFontFace: function that responsible to set font face css syntax

        args:
            - _withStyleTag(bool): if it `True`, return CSS syntax with <style>

        
        """
        for filename, weight in config.font_weights.items():
            file_path = os.path.join(config.fontsPath, filename)
            if not os.path.exists(file_path):
                continue
            
            # تحويل الملف إلى Base64
            b64_string = self._fontToBase64(file_path)
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

