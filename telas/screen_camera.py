from kivy.uix.screenmanager import Screen

import screen_home as home

class CameraScreen(Screen):
    camera_resolution = ""
    def set_camera_resolution(self):
        self.camera_resolution = self.ids.input_teste.text
        print(self.camera_resolution)
    def camera_start(self):
        home.HomeScreen.mount_camera()