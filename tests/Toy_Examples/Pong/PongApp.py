# PongApp.py from https://kivy.org/doc/stable/tutorials/pong.html
# Provided as courtesy for ad hoc testing.

import kivy
kivy.require('2.3.1')

from kivy.app import App
from kivy.uix.widget import Widget

class PongGame(Widget):
    pass

class PongApp(App):
    def build(self):
        return PongGame()
    
    
if __name__ == "__main__":
    PongApp().run()