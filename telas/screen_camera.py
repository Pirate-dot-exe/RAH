from kivy.uix.screenmanager import Screen

class CameraScreen(Screen):
    camera_resolution = ""
    def set_camera_resolution(self):
        self.camera_resolution = self.ids.input_teste.text
        print(self.camera_resolution)