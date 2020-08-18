from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.popup import Popup
from kivy.graphics import Rectangle, Line, Color
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.factory import Factory
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics.texture import Texture
from random import random
from array import array

from PIL import Image

import io

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    

#################################################################################

class DrawingWidget(Widget):
    target_colour_rgb = ListProperty([0, 0, 0])

    def update(self, texture, width, height):
        with self.canvas:
            Rectangle(texture=texture, pos=self.pos, size=(width, height))

    def on_touch_down(self, touch):
        super(DrawingWidget, self).on_touch_down(touch)

class Interface(BoxLayout):
    pass


class FelicityApp(App):
    loadfile = ObjectProperty(None)
    defaultPath = StringProperty('.')
    
    def build(self):
        root_widget = Interface()
        return root_widget
    def load_file_menu(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title='Load', content=content,
                      size_hint=(0.9, 0.9))
        self._popup.open()
        
    def load(self, path, filename):
        print(filename[0])
        img = Image.open(filename[0])
        width, height = img.size

        imgArr = list(img.getdata())
        imgArr = [int(i[0]) for i in imgArr for ch in range(3)]
        
        arr = array('B', imgArr)
        texture = Texture.create(size=(width, height))
        texture.blit_buffer(arr, colorfmt='rgb',
                            bufferfmt='ubyte')

        self.root.ids.draw_widget.update(texture, width, height)
        self.dismiss_popup()

    def dismiss_popup(self):
        self._popup.dismiss()
        

if __name__ == "__main__":
    FelicityApp().run()
