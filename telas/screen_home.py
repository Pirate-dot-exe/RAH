import sys
import platform

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


class HomeScreen(Screen):
    def mount_camera(self):
        if platform.system() == 'Windows':
            print("trying to mount camera")
            try:
                from kivy.uix.camera import Camera #Camera / -- (Deprecated for recent android devices)
                self.ids.home_main_box.remove_widget(self.ids.camera_image)
                win_camera = Camera(
                    resolution = (640, 480),
                    play = True
                )
                self.ids.home_main_box.add_widget(win_camera)
            except Exception as err:
                raise MountCameraException("Nao foi possivel montar a camera no dispositivo") from err
            

        elif platform == 'android':
            from kivy.uix.image import Image
            from kivy.clock import Clock
            from plyer import camera

            
    #def capture(self):
    #    camera = self.ids['camera']
    #    timestr = time.strftime("%Y%m%d_%H%M%S")
    #    camera.export_to_png("IMG_{}.png".format(timestr))
    #    print("Captured")

    def quit(self):
        sys.exit("Application Closed by User Command")

class MountCameraException(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
    
    def __str__(self):
        return  f"{type(self).__name__}: {self.mensagem}"