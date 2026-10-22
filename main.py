from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import os

# محاولة استيراد متصفح الويب المدمج لـ Kivy
try:
    from kivy.uix.webview import WebView
except ImportError:
    WebView = None

class MakeenApp(App):
    def build(self):
        self.title = "Makeen Bank & Empire"
        layout = BoxLayout(orientation='vertical')
        
        # مسار ملف الويب المحلي (bank.html)
        # سنجعل التطبيق يشير إلى صفحة البنك الرئيسية
        path_to_html = os.path.abspath("../bank.html")
        url = f"file:///{path_to_html}"
        
        if WebView:
            # فتح الصفحة عبر متصفح التطبيق المدمج
            webview = WebView(url=url)
            layout.add_widget(webview)
        else:
            # رسالة بديلة في حال تشغيله على سطح المكتب للاختبار
            from kivy.uix.label import Label
            lbl = Label(text="[INFO] WebView requires Android build.\nPath: " + url, markup=True)
            layout.add_widget(lbl)
            
        return layout

if __name__ == '__main__':
    MakeenApp().run()