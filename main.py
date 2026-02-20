from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window

# لون الخلفية
Window.clearcolor = (0.05, 0.02, 0.1, 1)


class AnimeCard(BoxLayout):
    def __init__(self, title, rating, **kwargs):
        super().__init__(
            orientation='vertical',
            size_hint=(None, None),
            size=(165, 250),
            spacing=5,
            padding=8,
            **kwargs
        )

        # خلفية بنفسجية منحنية
        with self.canvas.before:
            Color(0.12, 0.06, 0.25, 1)
            self.bg = RoundedRectangle(radius=[18])
        self.bind(pos=self.update_bg, size=self.update_bg)

        # بديل الصورة (مربع رمادي ثابت)
        img_placeholder = Label(
            text="IMAGE",
            size_hint_y=0.6,
            color=(0.7, 0.7, 0.7, 1)
        )
        self.add_widget(img_placeholder)

        # اسم الأنمي
        self.add_widget(Label(
            text=title,
            font_size='13sp',
            size_hint_y=0.15,
            color=(1, 1, 1, 1)
        ))

        # التقييم
        self.add_widget(Label(
            text=f"⭐ {rating}",
            font_size='11sp',
            size_hint_y=0.1,
            color=(1, 0.8, 0, 1)
        ))

        # زر بدون plyer
        watch_btn = Button(
            text="WATCH",
            size_hint_y=0.15,
            background_normal="",
            background_color=(0.5, 0, 1, 1)
        )
        self.add_widget(watch_btn)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size


class EmperorApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

        # الهيدر
        header = BoxLayout(size_hint_y=0.12, padding=10, spacing=10)
        header.add_widget(Label(
            text="👑 EMPEROR",
            font_size='22sp',
            color=(0.7, 0.2, 1, 1),
            size_hint_x=0.4
        ))

        search_input = TextInput(
            hint_text="Search Anime...",
            multiline=False,
            background_color=(0.1, 0.05, 0.2, 1),
            foreground_color=(1, 1, 1, 1)
        )

        header.add_widget(search_input)
        root.add_widget(header)

        # المحتوى
        main_scroll = ScrollView()
        main_content = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            padding=15,
            spacing=25
        )
        main_content.bind(minimum_height=main_content.setter('height'))

        # Trending
        main_content.add_widget(Label(
            text="🔥 TRENDING NOW",
            font_size='18sp',
            size_hint_y=None,
            height=30
        ))

        trend_scroll = ScrollView(
            size_hint_y=None,
            height=260,
            do_scroll_x=True,
            do_scroll_y=False
        )

        trend_grid = GridLayout(
            rows=1,
            size_hint_x=None,
            spacing=15
        )
        trend_grid.bind(minimum_width=trend_grid.setter('width'))

        anime_data = [
            ("Demon Slayer", "4.9"),
            ("Jujutsu Kaisen", "4.8"),
            ("Solo Leveling", "4.9")
        ]

        for title, rate in anime_data:
            trend_grid.add_widget(AnimeCard(title, rate))

        trend_scroll.add_widget(trend_grid)
        main_content.add_widget(trend_scroll)

        # All Animes
        main_content.add_widget(Label(
            text="📂 ALL ANIMES",
            font_size='18sp',
            size_hint_y=None,
            height=30
        ))

        all_grid = GridLayout(
            cols=2,
            size_hint_y=None,
            spacing=15
        )
        all_grid.bind(minimum_height=all_grid.setter('height'))

        for i in range(5):
            for title, rate in anime_data:
                all_grid.add_widget(AnimeCard(title, rate))

        main_content.add_widget(all_grid)
        main_scroll.add_widget(main_content)
        root.add_widget(main_scroll)

        # الفوتر
        footer = BoxLayout(size_hint_y=0.1, padding=8)
        footer.add_widget(Button(
            text="🏠",
            background_normal="",
            background_color=(0.4, 0, 0.8, 1),
            size_hint_x=0.2
        ))
        footer.add_widget(Label(text=""))
        root.add_widget(footer)

        return root


if __name__ == "__main__":
    EmperorApp().run()
