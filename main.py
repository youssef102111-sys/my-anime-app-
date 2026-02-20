from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.label = Label(text="Hello Youssef 🔥", font_size=30)
        self.add_widget(self.label)

        btn = Button(text="اضغط هنا", size_hint=(1, 0.3))
        btn.bind(on_press=self.change_text)
        self.add_widget(btn)

    def change_text(self, instance):
        self.label.text = "اشتغل التطبيق بنجاح 💪🔥"


class MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    MyApp().run()
