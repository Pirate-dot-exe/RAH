#support
#s://github.com/inclement/colour-blind-camera/blob/master/camera2/main.pyhttp

import permissions

import sys
#Processamento de Imagem / Image Processing
#import cv2

#import time

import kivy 
kivy.require('1.9.1')
from kivy.app import App
from kivy.lang import Builder
#Gerenciamento Multi-Telas / MultiScreen Management
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
#Exibição de Imagens / Images Exibition
from kivy.uix.image import Image
#Barra de Progresso / Progress Bar
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput

from kivy.uix.button import Button
from kivy.utils import platform

class LoadingScreen(Screen):
    pb = ProgressBar(max=100)
    pb.value = 0

    def progressbar(self, dt):
        if self.ids.pb.value < 100:
            self.ids.pb.value += 1
            self.ids.progress_info.text = f"Loading... {int(self.ids.pb.value)}%"
            Clock.schedule_once(self.progressbar, 1/25)
        else:
            self.ids.progress_info.text = "Loading Complete! (wait a minute)"
            sm.current = 'home'
    
    def callback_func(self):
        Clock.schedule_once(self.progressbar, 1/25)

    permissions.ask_permission()

class HomeScreen(Screen):
    def mount_camera(self):
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
    def destroy_loading(self):
        loading_screen = LoadingScreen(name='loading')
        sm.remove_widget(loading_screen)

    def quit(self):
        sys.exit("Application Closed by User Command")

class CameraScreen(Screen):
    camera_resolution = ""
    def set_camera_resolution(self):
        self.camera_resolution = self.ids.input_teste.text
        print(self.camera_resolution)

class BluetoothScreen(Screen):
    import blt_func as blt

    def search_devices(self):
        if platform=='win':
            self.ids.blt_device_list.clear_widgets()
            devices_found, self.ids.devices_found.text = self.blt.search_new_devices()
            if len(devices_found) > 0:
                self.ids.blt_device_list.remove_widget(self.ids.devices_found)

                for device in devices_found:
                    self.ids.blt_device_list.add_widget(
                        Button(
                            #id = str(device[0]),
                            text="connect to " + str(device[1]),
                            on_press=(lambda x: self.try_connection(str(device[0])))
                        )
                    )
                    #self.ids.str(device[0]).bind(on_press=self.try_connection)
            elif platform=='android':
                self.ids.devices_found.text = "Sorry, no implemented yet :p"
                    
    def try_connection(self, addr):
        print("try_connection")
        self.blt.try_connection(addr)

class WindowManager(ScreenManager):
    pass

class ScreenLoader(App):

    def build(self):
        permissions.ask_permission()

        global sm 
        sm = ScreenManager()
        loading_screen = LoadingScreen(name='loading')
        home_screen = HomeScreen(name='home')
        camera_screen = CameraScreen(name='camera_config')
        bluetooth_screen = BluetoothScreen(name='bluetooth_config')
        sm.add_widget(loading_screen)
        sm.add_widget(home_screen)
        sm.add_widget(camera_screen)
        sm.add_widget(bluetooth_screen)
        return sm

if __name__ == '__main__':
    ScreenLoader().run()