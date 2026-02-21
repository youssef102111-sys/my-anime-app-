from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window
from plyer import browser

Window.clearcolor = (0.05, 0.02, 0.1, 1)

class AnimeCard(BoxLayout):
    def __init__(self, title, rating, img_url, link, **kwargs):
        super().__init__(orientation='vertical', size_hint=(None, None), size=(165, 270), spacing=5, padding=5, **kwargs)
        with self.canvas.before:
            Color(0.12, 0.06, 0.25, 1)
            self.bg = RoundedRectangle(radius=[18])
        self.bind(pos=self.update_bg, size=self.update_bg)

        self.add_widget(AsyncImage(source=img_url, size_hint_y=0.65))
        self.add_widget(Label(text=title, bold=True, font_size='13sp', size_hint_y=0.1, color=(1, 1, 1, 1)))
        self.add_widget(Label(text=f"⭐ {rating}", font_size='11sp', size_hint_y=0.08, color=(1, 0.8, 0, 1)))
        
        watch_btn = Button(text="WATCH NOW", size_hint_y=0.17, background_normal="", background_color=(0.5, 0, 1, 1), bold=True)
        watch_btn.bind(on_release=lambda x: browser.open(link))
        self.add_widget(watch_btn)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

class EmperorApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

        # هيدر البحث
        header = BoxLayout(size_hint_y=0.12, padding=10, spacing=10)
        header.add_widget(Label(text="👑 EMPEROR", font_size='22sp', bold=True, color=(0.7, 0.2, 1, 1), size_hint_x=0.4))
        search_input = TextInput(hint_text="Search Anime...", multiline=False, background_color=(0.1, 0.05, 0.2, 1), foreground_color=(1,1,1,1))
        header.add_widget(search_input)
        root.add_widget(header)

        # السكرول العامودي الرئيسي
        main_scroll = ScrollView()
        main_content = BoxLayout(orientation='vertical', size_hint_y=None, padding=15, spacing=25)
        main_content.bind(minimum_height=main_content.setter('height'))

        # بيانات أنمي حقيقية
        anime_data = [
            ("Demon Slayer", "4.9", "https://i.imgur.com/8Km9tLL.jpg", "https://www.crunchyroll.com/demon-slayer"),
            ("Jujutsu Kaisen", "4.8", "https://i.imgur.com/VZ6YVbR.jpg", "https://www.crunchyroll.com/jujutsu-kaisen"),
            ("Solo Leveling", "4.9", "https://i.imgur.com/5tj6S7Ol.jpg", "https://www.crunchyroll.com/solo-leveling"),
            ("One Piece", "4.9", "https://i.imgur.com/8Km9tLL.jpg", "https://www.crunchyroll.com/one-piece"),
            ("Attack on Titan", "4.8", "https://i.imgur.com/VZ6YVbR.jpg", "https://www.crunchyroll.com/attack-on-titan"),
            ("Chainsaw Man", "4.7", "https://i.imgur.com/5tj6S7Ol.jpg", "https://www.crunchyroll.com/chainsaw-man")
        ]

        # قسم التريند (أفقي)
        main_content.add_widget(Label(text="🔥 TRENDING", bold=True, font_size='18sp', size_hint_y=None, height=30))
        trend_scroll = ScrollView(size_hint_y=None, height=280, do_scroll_x=True, do_scroll_y=False)
        trend_grid = GridLayout(rows=1, size_hint_x=None, spacing=15)
        trend_grid.bind(minimum_width=trend_grid.setter('width'))
        for title, rate, img, link in anime_data:
            trend_grid.add_widget(AnimeCard(title, rate, img, link))
        trend_scroll.add_widget(trend_grid)
        main_content.add_widget(trend_scroll)

        # قسم المكتبة الكبرى (عامودي بـ 100 أنمي)
        main_content.add_widget(Label(text="📂 ALL LIBRARY", bold=True, font_size='18sp', size_hint_y=None, height=30))
        all_grid = GridLayout(cols=2, size_hint_y=None, spacing=15)
        all_grid.bind(minimum_height=all_grid.setter('height'))
        
        # تكرار القائمة 20 مرة ليصبح عندك 120 أنمي في السكرول
        for i in range(20):
            for title, rate, img, link in anime_data:
                all_grid.add_widget(AnimeCard(title, rate, img, link))

        main_content.add_widget(all_grid)
        main_scroll.add_widget(main_content)
        root.add_widget(main_scroll)

        return root

if __name__ == "__main__":
    EmperorApp().run()
