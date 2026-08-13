from style import style
import os, base64

class htmlBody:
    def __init__(self, htmlTemplate:str, data:dict):
        self.ok   = True
        self.data = data

        self.htmlTemplatePath = os.path.join('htmlTemplate', htmlTemplate)
        if not os.path.exists(self.htmlTemplatePath):
            self.ok = False
            print(f"[style]: `{self.htmlTemplatePath}` is not exists!")

        
    def _setCard(self):
        cardHeader = """ 
        <div class="card-header">  
            <!-- تصنيف المقال -->
            <div class="badge">الدعم وحلول مشاكل المستخدم</div>
            
            <!-- فاصل -->
            <div class="divider"></div>

            <!-- معلومات بسيطة عن كاتب المقال -->
            <div class="user-info">
                <span class="username">t4rik</span>
                <img class="avatar" src="./logo/9345_2.png">
            </div>

            <!-- فاصل -->
            <div class="divider"></div>
            
            <!-- شعار مجتمع أسس-->
            <img src="./logo/logo-text-dark.svg" alt="Logo" class="logo">
        </div>"""
        
        cardBody = """
        <div class="card-body">
            <h1>خط اليمامة: جيل جديد من خطوط النسخ للشاشات والإعلان</h1>
            <p>في عالم الخط العربي الرقمي، لا يكفي أن يكون الخط جميلاً؛ بل يجب أن يكون واضحاً، مرناً، سريعاً في العرض، وقادراً على الحفاظ على شخصيته في مختلف الأحجام والسياقات. من هنا يأتي خط اليمامة، وهو خط نسخ متغيّر صُمّم للإعلان واللافتات والنصوص، جامعاً بين أناقة النسخ التقليدي ومتطلبات التصميم الرقمي الحديث ......</p>
        </div>"""

        cardBase   = """<div class="card">\n{cardHeader}\n{cardBody}\n</div>"""
        
    
    def setHTML(self):
        htmlHead     = """<head> <link rel="stylesheet" href="style.css"> </head>"""
        htmlBody     = """<body>{}</body>"""
        htmlFullBody = f"""<!DOCTYPE html>\n<<html lang="ar">\n{htmlHead}\n{htmlBody}</html>"""

