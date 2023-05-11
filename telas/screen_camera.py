from kivy.uix.screenmanager import Screen
from kivy.uix.slider import Slider

class CameraScreen(Screen):
    camera_resolution = ""
    def set_camera_resolution(self):
        self.camera_resolution = self.ids.input_teste.text
        print(self.camera_resolution)

    