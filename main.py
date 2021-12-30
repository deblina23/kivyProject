import kivy
from kivy.app import App
from kivy.uix.label import Label


class FirstKivyApp(App):

    def build(self):
        return Label(text="Hello Deblina!!!!")


if __name__ == "__main__":
    FirstKivyApp().run()
