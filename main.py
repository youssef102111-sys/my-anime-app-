from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from plyer import notification
import webbrowser

class EmperorAnimeApp(App):
    def build(self):
        # إعداد سمة الألوان: أسود وبنفسجي برق
        Window.clearcolor = get_color_from_hex('#000000') 
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # --- الجزء العلوي (العنوان والبحث) ---
        header = BoxLayout(size_hint_y=0.1)
        header.add_widget(Label(
            text='EMPEROR ANIME LIST', 
            font_size='24sp', 
            bold=True, 
            color=get_color_from_hex('#8A2BE2')
        ))
        search_btn = Button(
            text='🔍', 
            size_hint_x=0.2, 
            background_color=(0,0,0,0), 
            color=get_color_from_hex('#8A2BE2')
        )
        header.add_widget(search_btn)
        self.main_layout.add_widget(header)

        # --- قائمة الأنمي (الصور والمواعيد) ---
        scroll = ScrollView(size_hint_y=0.8)
        self.anime_list_container = BoxLayout(orientation='vertical', size_hint_y=None, spacing=25)
        self.anime_list_container.bind(minimum_height=self.anime_list_container.setter('height'))

        # بيانات الأنمي التجريبية
        animes = [
            ("One Piece", "Next Ep: Sunday 09:00", "https://example.com/op"),
            ("Solo Leveling", "Next Ep: Saturday 18:00", "https://example.com/sl"),
            ("Demon Slayer", "New Season Coming Soon", "https://example.com/ds")
        ]

        for name, schedule, link in animes:
            # حاوية لكل بطاقة أنمي
            card = BoxLayout(orientation='vertical', size_hint_y=None, height=160, padding=10)
            
            # زر الأنمي مع عداد الوقت الملون
            anime_btn = Button(
                text=f"[b]{name}[/b]\n[color=8A2BE2]{schedule}[/color]", 
                markup=True,
                background_normal='',
                background_color=get_color_from_hex('#121212'),
                font_size='20sp',
                halign='center'
            )
            # عند الضغط يظهر خيار الجودات
            anime_btn.bind(on_release=lambda x, n=name: self.open_quality_menu(n))
            
            card.add_widget(anime_btn)
            self.anime_list_container.add_widget(card)

        scroll.add_widget(self.anime_list_container)
        self.main_layout.add_widget(scroll)

        # --- شريط التنقل (علامة بيت واحدة فقط) ---
        footer = BoxLayout(size_hint_y=0.1, padding=5)
        home_icon = Button(
            text='🏠', 
            size_hint_x=0.2, 
            background_normal='',
            background_color=get_color_from_hex('#4B0082')
        )
        footer.add_widget(home_icon)
        footer.add_widget(Label(text='')) # موازن للفراغ
        self.main_layout.add_widget(footer)

        return self.main_layout

    def open_quality_menu(self, title):
        # نافذة الجودات والسيرفرات البنفسجية
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        layout.add_widget(Label(text=f"Quality Settings for {title}", bold=True, color=get_color_from_hex('#8A2BE2')))
        
        options = ['1080p (FHD) ⚡', '720p (HD) ⚡', '480p (SD) ⚡', 'Server VIP']
        for opt in options:
            btn = Button(text=opt, background_color=get_color_from_hex('#4B0082'))
            btn.bind(on_release=lambda x: webbrowser.open("https://www.google.com"))
            layout.add_widget(btn)

        popup = Popup(
            title='Emperor Player', 
            content=layout, 
            size_hint=(0.9, 0.7),
            background_color=get_color_from_hex('#000000')
        )
        popup.open()
        
        # إرسال إشعار فوري عند المشاهدة
        self.trigger_notification(title)

    def trigger_notification(self, anime_name):
        try:
            notification.notify(
                title='Emperor Anime',
                message=f'Starting {anime_name}... New episode alert active! ⚡',
                timeout=10
            )
        except:
            pass

if __name__ == '__main__':
    EmperorAnimeApp().run()
