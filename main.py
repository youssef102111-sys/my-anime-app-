from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import AsyncImage
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.animation import Animation
from plyer import browser, notification
from datetime import datetime, timedelta


Window.clearcolor = get_color_from_hex('#000000')


# ================= SPLASH SCREEN =================
class SplashScreen(Screen):
    def on_enter(self):
        self.clear_widgets()
        layout = BoxLayout()
        title = Label(
            text="EMPEROR ANIME",
            font_size="40sp",
            bold=True,
            color=get_color_from_hex('#8A2BE2'),
            opacity=0
        )
        layout.add_widget(title)
        self.add_widget(layout)

        anim = Animation(opacity=1, duration=2)
        anim.start(title)

        Clock.schedule_once(self.go_main, 3)

    def go_main(self, dt):
        self.manager.current = "main"


# ================= MAIN SCREEN =================
class MainScreen(Screen):

    def on_enter(self):
        self.clear_widgets()
        self.build_ui()

    def build_ui(self):

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        header = Label(
            text='EMPEROR ANIME LIST',
            font_size='24sp',
            bold=True,
            color=get_color_from_hex('#8A2BE2'),
            size_hint_y=0.1
        )
        main_layout.add_widget(header)

        scroll = ScrollView(size_hint_y=0.8)

        container = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            spacing=20
        )
        container.bind(minimum_height=container.setter('height'))

        future_time = datetime.now() + timedelta(hours=24)

        animes = [
            ("One Piece",
             "https://i.imgur.com/8Km9tLL.jpg",
             "https://example.com"),
            ("Solo Leveling",
             "https://i.imgur.com/VZ6YVbR.jpg",
             "https://example.com"),
            ("Demon Slayer",
             "https://i.imgur.com/5tj6S7Ol.jpg",
             "https://example.com")
        ]

        for name, image_url, link in animes:

            card = BoxLayout(
                orientation='vertical',
                size_hint_y=None,
                height=260,
                padding=10,
                spacing=5
            )

            img = AsyncImage(
                source=image_url,
                size_hint_y=0.7
            )

            countdown_label = Label(
                color=get_color_from_hex('#8A2BE2'),
                font_size='16sp'
            )

            Clock.schedule_interval(
                lambda dt, lbl=countdown_label, ft=future_time:
                self.update_countdown(lbl, ft),
                1
            )

            btn = Button(
                text=name,
                size_hint_y=0.2,
                background_normal='',
                background_color=get_color_from_hex('#121212')
            )

            btn.bind(on_release=lambda x, l=link, n=name:
                     self.open_quality_menu(n, l))

            card.add_widget(img)
            card.add_widget(countdown_label)
            card.add_widget(btn)

            container.add_widget(card)

        scroll.add_widget(container)
        main_layout.add_widget(scroll)

        self.add_widget(main_layout)

    # ================= COUNTDOWN =================
    def update_countdown(self, label, future_time):
        remaining = future_time - datetime.now()

        if remaining.total_seconds() > 0:
            hours, remainder = divmod(int(remaining.total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60)
            label.text = f"Next Episode In: {hours:02}:{minutes:02}:{seconds:02}"
        else:
            label.text = "Episode Released! ⚡"

    # ================= POPUP =================
    def open_quality_menu(self, title, link):

        layout = BoxLayout(
            orientation='vertical',
            spacing=10,
            padding=20
        )

        layout.add_widget(Label(
            text=f"Watch {title}",
            bold=True,
            color=get_color_from_hex('#8A2BE2')
        ))

        qualities = ['1080p ⚡', '720p ⚡', '480p ⚡']

        for q in qualities:
            btn = Button(
                text=q,
                background_normal='',
                background_color=get_color_from_hex('#4B0082')
            )
            btn.bind(on_release=lambda x, url=link: browser.open(url))
            layout.add_widget(btn)

        popup = Popup(
            title='Emperor Player',
            content=layout,
            size_hint=(0.9, 0.7)
        )

        popup.open()

        try:
            notification.notify(
                title="Emperor Anime",
                message=f"Starting {title} ⚡",
                timeout=5
            )
        except:
            pass


# ================= APP =================
class EmperorAnimeApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name="splash"))
        sm.add_widget(MainScreen(name="main"))
        return sm


if __name__ == '__main__':
    EmperorAnimeApp().run()
