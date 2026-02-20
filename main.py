from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class AnimeApp(App):
    def build(self):
        # لون الخلفية (أسود فخم)
        Window.clearcolor = get_color_from_hex('#000000')
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # عنوان التطبيق بلون البرق البنفسجي
        title = Label(
            text='Anime Emperor',
            font_size='40sp',
            color=get_color_from_hex('#8A2BE2'), # بنفسجي كهربائي
            bold=True
        )
        
        # زرار للدخول في عالم الأنمي
        btn = Button(
            text='Enter the Realm',
            size_hint=(None, None),
            size=(250, 60),
            pos_hint={'center_x': 0.5},
            background_color=get_color_from_hex('#4B0082')
        )
        
        layout.add_widget(title)
        layout.add_widget(btn)
        
        return layout

if __name__ == '__main__':
    AnimeApp().run()
