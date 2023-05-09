import sys
import cv2

from kivy import platform
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.graphics.texture import Texture


class OpenCVCamera(Image):
    def __init__(self, capture, **kwargs):
        super(OpenCVCamera, self).__init__(**kwargs)
        self.capture = capture

    def capture_frame(self, dt):
        ret, frame = self.capture.read()
        if ret:
            buf = cv2.flip(frame, 0).tostring()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]))
            texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.texture = texture
    
    def release(self):
        self.capture.release()
        self.ids.camera_box.clear_widgets()

class HomeScreen(Screen):
    camera_status = 'off'

    def mount_camera(self):
        if self.camera_status == 'off':
            if platform == 'win':
                print("trying to mount camera")
                try:
                    self.capture = cv2.VideoCapture(0)
                    self.opencv_camera = OpenCVCamera(capture=self.capture)
                    Clock.schedule_interval(self.opencv_camera.capture_frame, 1.0/30)    
                    self.ids.camera_box.add_widget(self.opencv_camera)
                    self.camera_status = 'on'
                    self.ids.camera_box.remove_widget(self.ids.camera_icon)
                except Exception as err:
                    camera_icon = Image(
                        source = 'images/camera.png'
                    )
                    self.ids.camera_box.add_widget(camera_icon)
                    raise MountCameraException("Nao foi possivel montar a camera no dispositivo") from err

            elif platform == 'android':
                pass     
    
    def unmount_camera(self):
        self.opencv_camera.release()
        self.camera_status = 'off'

    def play_stop_camera(self):
        if self.camera_status == 'off':
            self.mount_camera()
        elif self.camera_status == 'on':
            self.unmount_camera()

        pass

    def quit(self):
        sys.exit("Application Closed by User Command")

class MountCameraException(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
    
    def __str__(self):
        return  f"{type(self).__name__}: {self.mensagem}"