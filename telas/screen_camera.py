from kivy.uix.screenmanager import Screen
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.properties import NumericProperty

class CameraScreen(Screen):
    camera_resolution = ""
    red_value = NumericProperty(0)
    green_value = NumericProperty(0)
    blue_value = NumericProperty(0)

    def __init__(self, **kwargs):
        super(CameraScreen, self).__init__(**kwargs)
        self.custom_color_box = CustomColorBox()
        self.ids.color_box_layout.add_widget(self.custom_color_box)
        self.bind(red_value=self.update_color,
                  green_value=self.update_color,
                  blue_value=self.update_color
            )

    def set_camera_resolution(self):
        self.camera_resolution = self.ids.input_teste.text
        print(self.camera_resolution)

    def on_red_value(self, instance, value):
        self.ids.red_value_slider = value
    
    def on_green_value(self, instance, value):
        self.ids.green_value_slider = value

    def on_blue_value(self, instance, value):
        self.ids.blue_value_slider = value

    def update_color(self, *args):
        self.custom_color_box.update_color(
            self.red_value,
            self.green_value,
            self.blue_value
        )

class CustomColorBox(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            self.rect_color = Color(0, 0, 0, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)
        self.update_color

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def update_color(self, *args):
        self.set_color(self.red_value/255, self.green_value/255, self.blue_value/255)

    def set_color(self, red, green, blue):
        self.rect_color.rgba = (red/255, green/255, blue/255, 1)