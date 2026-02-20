from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window

Window.clearcolor = (0.05, 0.02, 0.1, 1)


class AnimeCard(BoxLayout):
    def __init__(self, title, rating, image_path, **kwargs):
        super().__init__(orientation='vertical',
                         size_hint=(None, None),
                         size=(180, 260),
                         padding=8,
                         spacing=5,
                         **kwargs)

        with self.canvas.before:
            Color(0.15, 0.05, 0.25, 1)
            self.bg = RoundedRectangle(radius=[20])
        self.bind(pos=self.update_bg, size=self.update_bg)

        img = Image(source=image_path)

        name = Label(
            text=f"[b]{title}[/b]",
            markup=True,
            size_hint=(1, 0.2),
            color=(1, 1, 1, 1)
        )

        rating_lbl = Label(
            text=f"⭐ {rating}",
            size_hint=(1, 0.15),
            color=(1, 0.8, 0.2, 1)
        )

        btn = Button(
            text="WATCH NOW",
            size_hint=(1, 0.2),
            background_normal="",
            background_color=(0.6, 0.2, 1, 1)
        )

        self.add_widget(img)
        self.add_widget(name)
        self.add_widget(rating_lbl)
        self.add_widget(btn)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size


class MainApp(App):
    def build(self):

        root = BoxLayout(orientation="vertical", padding=10, spacing=15)

        title = Label(
            text="[b]🔥 EMPEROR ANIME[/b]",
            markup=True,
            font_size=26,
            size_hint=(1, 0.1),
            color=(1, 1, 1, 1)
        )

        scroll = ScrollView(size_hint=(1, 0.9))

        grid = GridLayout(
            cols=2,
            spacing=15,
            size_hint_y=None,
            padding=10
        )
        grid.bind(minimum_height=grid.setter('height'))

        animes = [
            ("Demon Slayer", "4.9", "images/demon.jpg"),
            ("Jujutsu Kaisen", "4.8", "images/jujutsu.jpg"),
            ("Chainsaw Man", "4.7", "images/chainsaw.jpg"),
            ("Attack on Titan", "4.8", "images/aot.jpg"),
        ]

        for name, rate, img in animes:
            grid.add_widget(AnimeCard(name, rate, img))

        scroll.add_widget(grid)

        root.add_widget(title)
        root.add_widget(scroll)

        return root


if __name__ == "__main__":
    MainApp().run()
