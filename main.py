from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window
from kivy.clock import Clock
from datetime import datetime, timedelta
import webbrowser

# إعداد لون الخلفية (أسود ملكي)
Window.clearcolor = (0.05, 0.02, 0.1, 1)

class AnimeCard(BoxLayout):
    def __init__(self, title, rating, image_url, release_time, **kwargs):
        super().__init__(orientation='vertical', size_hint=(None, None), size=(180, 280), padding=10, spacing=5, **kwargs)
        
        self.release_time = release_time
        
        with self.canvas.before:
            Color(0.1, 0.05, 0.2, 1) # خلفية البطاقة بنفسجي غامق
            self.bg = RoundedRectangle(radius=[20])
        self.bind(pos=self.update_bg, size=self.update_bg)

        # بوستر الأنمي
        img = AsyncImage(source=image_url, size_hint=(1, 0.6))
        
        # الاسم والتقييم
        name = Label(text=f"[b]{title}[/b]", markup=True, size_hint=(1, 0.1), font_size='14sp')
        stars = Label(text=f"⭐ {rating}", size_hint=(1, 0.05), color=(1, 0.8, 0, 1), font_size='12sp')
        
        # العداد التنازلي (ميزة الـ Countdown)
        self.timer_label = Label(text="", size_hint=(1, 0.1), color=(0.6, 0.2, 1, 1), font_size='11sp')
        Clock.schedule_interval(self.update_timer, 1)

        # زر المشاهدة (Watch Now)
        watch_btn = Button(text="WATCH NOW", size_hint=(1, 0.15), background_normal="", 
                           background_color=(0.5, 0, 1, 1), font_size='12sp', bold=True)
        watch_btn.bind(on_release=lambda x: webbrowser.open("https://google.com"))

        self.add_widget(img)
        self.add_widget(name)
        self.add_widget(stars)
        self.add_widget(self.timer_label)
        self.add_widget(watch_btn)

    def update_timer(self, dt):
        remaining = self.release_time - datetime.now()
        if remaining.total_seconds() > 0:
            h, rem = divmod(int(remaining.total_seconds()), 3600)
            m, s = divmod(rem, 60)
            self.timer_label.text = f"{h:02d}:{m:02d}:{s:02d} Left"
        else:
            self.timer_label.text = "NEW EPISODE OUT! ⚡"

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

class EmperorApp(App):
    def build(self):
        root = BoxLayout(orientation="vertical")

        # العنوان العلوي
        root.add_widget(Label(text="[b]🔥 TRENDING NOW[/b]", markup=True, size_hint_y=0.1, font_size='22sp'))

        # منطقة المحتوى القابلة للتمرير
        scroll = ScrollView(size_hint_y=0.8)
        grid = GridLayout(cols=2, spacing=15, size_hint_y=None, padding=15)
        grid.bind(minimum_height=grid.setter('height'))

        # بيانات الأنمي (روابط الصور ومواعيد الحلقات)
        future = datetime.now() + timedelta(hours=24)
        animes = [
            ("Demon Slayer", "4.9", "https://i.imgur.com/8Km9tLL.jpg", future),
            ("Jujutsu Kaisen", "4.8", "https://i.imgur.com/VZ6YVbR.jpg", future + timedelta(hours=5)),
            ("Chainsaw Man", "4.7", "https://i.imgur.com/5tj6S7Ol.jpg", future + timedelta(days=1)),
            ("Attack on Titan", "4.8", "https://i.imgur.com/8Km9tLL.jpg", future + timedelta(hours=10))
        ]

        for name, rate, img, time in animes:
            grid.add_widget(AnimeCard(name, rate, img, time))

        scroll.add_widget(grid)
        root.add_widget(scroll)

        # شريط التنقل السفلي (علامة بيت واحدة فقط)
        footer = BoxLayout(size_hint_y=0.1, padding=10)
        home_btn = Button(text="🏠", size_hint_x=0.2, background_normal="", background_color=(0.3, 0, 0.6, 1))
        footer.add_widget(home_btn)
        footer.add_widget(Label(text="")) # فراغ للتنسيق
        root.add_widget(footer)

        return root

if __name__ == "__main__":
    EmperorApp().run()
