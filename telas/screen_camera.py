from kivy.uix.screenmanager import Screen
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.properties import NumericProperty

class CameraScreen(Screen):
    camera_resolution = ""

    def __init__(self, **kwargs):
        super(CameraScreen, self).__init__(**kwargs)
        self.custom_color_box = self.ids.color_box

    def set_camera_resolution(self):
        self.camera_resolution = self.ids.input_teste.text
        print(self.camera_resolution)

    def update_color(self):
        print(self.ids.red_value.value)
        self.ids.color_box.set_color(
            self.ids.red_value.value,
            self.ids.green_value.value,
            self.ids.blue_value.value
        )

class CustomColorBox(Widget):
    red_value = NumericProperty(0)
    green_value = NumericProperty(0)
    blue_value = NumericProperty(0)

    def __init__(self, **kwargs):
        super(CustomColorBox, self).__init__(**kwargs)
        self.bind(
            red_value=self.update_color,
            green_value=self.update_color,
            blue_value=self.update_color
        )
        with self.canvas.before:
            self.rect_color = Color(1, 0, 0, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def update_color(self, *args):
        self.set_color(self.red_value, self.green_value, self.blue_value)

    def set_color(self, red, green, blue):
        self.rect_color.rgba = (red/255, green/255, blue/255, 1)