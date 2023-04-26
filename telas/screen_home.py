import sys

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class HomeScreen(Screen):
    def mount_camera(self):
        pass
        '''
        if platform == 'win':
            from kivy.uix.camera import Camera #Camera / -- (Deprecated for recent android devices)
            self.ids.home_main_box.remove_widget(self.ids.camera_image)
            self.ids.home_main_box.add_widget(
                Camera(
                    resolution = (640, 480),
                    play = True
                )
            )
        elif platform == 'android':
            from plyer import camera
        '''
            
    #def capture(self):
    #    camera = self.ids['camera']
    #    timestr = time.strftime("%Y%m%d_%H%M%S")
    #    camera.export_to_png("IMG_{}.png".format(timestr))
    #    print("Captured")

    def quit(self):
        sys.exit("Application Closed by User Command")