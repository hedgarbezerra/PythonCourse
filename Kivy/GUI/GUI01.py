import os
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
#os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'


class Home(App):
    def build(self):
        return Button(text='Hello World')


Home().run()
