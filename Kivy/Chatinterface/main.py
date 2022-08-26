from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
Builder.load_file("design.kv")


class Chatwindow(Widget):
    button = ObjectProperty(None)


class Send_Button(Widget):
    def pressed(self):
        print("Der Schmerz ist unerträglich")


class Text_box(Widget):
    def pressed(self):
        print("Der Schmerz ist unerträglich")


class Chatinterface(App):
    def build(self):
        return Chatwindow()


Chatinterface().run()
