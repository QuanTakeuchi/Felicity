from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.popup import Popup
from kivy.graphics import Rectangle, Line, Color
from kivy.properties import ListProperty, ObjectProperty
from kivy.factory import Factory
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics.texture import Texture
from random import random
from array import array

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


    
class DrawingWidget(Widget):
    target_colour_rgb = ListProperty([0, 0, 0])

    def on_touch_down(self, touch):
        super(DrawingWidget, self).on_touch_down(touch)

        size = 300 * 300 * 3
        buf = [int(x * 255 / size) for x in range(size)]
        arr = array('B', buf)
        texture = Texture.create(size=(300, 300))
        texture.blit_buffer(arr, colorfmt='rgb', bufferfmt='ubyte')
        arr[24] = arr[50] = 99


        with self.canvas:
            Rectangle(texture=texture, pos=self.pos, size=(300, 300))

    # def on_touch_down(self, touch):
    #     super(DrawingWidget, self).on_touch_down(touch)

    #     if not self.collide_point(*touch.pos):
    #         return

    #     with self.canvas:
    #         Color(*self.target_colour_rgb)
    #         self.line = Line(points=[touch.pos[0], touch.pos[1]], width=2)

    # def on_touch_move(self, touch):
    #     if not self.collide_point(*touch.pos):
    #         return

    #     self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]

class Interface(BoxLayout):
    pass


class FelicityApp(App):
    loadfile = ObjectProperty(None)
    
    def build(self):
        root_widget = Interface()
        return root_widget
    def load_file_menu(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title='Load', content=content,
                      size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        size = 300 * 300 * 3
        buf = [int(x * 255 / size) for x in range(size)]
        # initialize the array with the buffer values
        arr = array('B', buf)
        # now blit the array
        texture = Texture.create(size=(300, 300))
        texture.blit_buffer(arr, colorfmt='rgb', bufferfmt='ubyte')
        # now change some elements in the original array
        arr[24] = arr[50] = 99
        self.root.ids.draw_widget.rect = Rectangle(texture=texture,
                                                   size=(400, 400))
                
        self.dismiss_popup()

    def dismiss_popup(self):
        self._popup.dismiss()
        

if __name__ == "__main__":
    FelicityApp().run()
