# Hello World from https://kivy.org/doc/stable/guide/basic.html
# Provided as courtesy for ad hoc testing.

import kivy
kivy.require('2.3.1')

from kivy.app import App
from kivy.uix.label import Label

class HelloWorld(App):

    def build(self):
        return Label(text="Hello World")
    
if __name__ == "__main__":
    HelloWorld().run()