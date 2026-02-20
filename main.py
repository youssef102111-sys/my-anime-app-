from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window
from plyer import browser

# خلفية داكنة ملكية
Window.clearcolor = (0.05, 0.02, 0.1, 1)


class AnimeCard(BoxLayout):
    def __init__(self, title, rating, img_url, link, **kwargs):
        super().__init__(
            orientation='vertical',
            size_hint=(None, None),
            size=(170, 260),
            spacing=6,
            padding=6,
            **kwargs
        )

        with self.canvas.before:
            Color(0.15, 0.05, 0.3, 1)
            self.bg = RoundedRectangle(radius=[20])
            self.bind(pos=self.update_bg, size=self.update_bg)

        # صورة الأنمي
        self.add_widget(
            AsyncImage(source=img_url, size_hint_y=0.65)
        )

        # الاسم
        self.add_widget(
            Label(
                text=title,
                bold=True,
                font_size='14sp',
                size_hint_y=0.12,
                color=(1, 1, 1, 1)
            )
        )

        # التقييم
        self.add_widget(
            Label(
                text=f"⭐ {rating}",
                font_size='12sp',
                size_hint_y=0.08,
                color=(1, 0.8, 0, 1)
            )
        )

        # زر المشاهدة
        watch_btn = Button(
            text="WATCH",
            size_hint_y=0.15,
            background_normal="",
            background_color=(0.6, 0, 1, 1),
            bold=True
        )

        watch_btn.bind(on_release=lambda x: browser.open(link))
        self.add_widget(watch_btn)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size


class EmperorAnimeApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

        # عنوان التطبيق
        header = Label(
            text="👑 EMPEROR ANIME",
            font_size='24sp',
            bold=True,
            size_hint_y=0.1,
            color=(0.8, 0.3, 1, 1)
        )
        root.add_widget(header)

        scroll = ScrollView()

        content = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            padding=15,
            spacing=20
        )
        content.bind(minimum_height=content.setter('height'))

        # عنوان القسم
        content.add_widget(
            Label(
                text="🔥 TRENDING",
                bold=True,
                font_size='18sp',
                size_hint_y=None,
                height=30,
                color=(1, 1, 1, 1)
            )
        )

        # سكرول أفقي
        trend_scroll = ScrollView(
            size_hint_y=None,
            height=270,
            do_scroll_x=True,
            do_scroll_y=False
        )

        trend_grid = GridLayout(
            rows=1,
            size_hint_x=None,
            spacing=15
        )
        trend_grid.bind(minimum_width=trend_grid.setter('width'))

        # بيانات رسمية
        anime_data = [
            ("Demon Slayer", "4.9",
             "https://i.imgur.com/8Km9tLL.jpg",
             "https://www.crunchyroll.com/demon-slayer"),

            ("Jujutsu Kaisen", "4.8",
             "https://i.imgur.com/VZ6YVbR.jpg",
             "https://www.crunchyroll.com/jujutsu-kaisen"),

            ("Solo Leveling", "4.9",
             "https://i.imgur.com/5tj6S7Ol.jpg",
             "https://www.crunchyroll.com/solo-leveling")
        ]

        for title, rate, img, link in anime_data:
            trend_grid.add_widget(
                AnimeCard(title, rate, img, link)
            )

        trend_scroll.add_widget(trend_grid)
        content.add_widget(trend_scroll)

        scroll.add_widget(content)
        root.add_widget(scroll)

        return root


if __name__ == "__main__":
    EmperorAnimeApp().run()
