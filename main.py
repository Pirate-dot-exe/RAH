#support
#s://github.com/inclement/colour-blind-camera/blob/master/camera2/main.pyhttp

import sys
#Processamento de Imagem / Image Processing
#import cv2

#import time
from enum import Enum

import kivy 
kivy.require('1.9.1')
from kivy.app import App
from kivy.lang import Builder
#Gerenciamento Multi-Telas / MultiScreen Management
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
#Exibição de Imagens / Images Exibition
from kivy.uix.image import Image
#Camera / --
from kivy.uix.camera import Camera
#Barra de Progresso / Progress Bar
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput

#from android.permissions import request_permission, check_permission, Permission

class PermissionRequestState(Enum):
    UNKNOWN = "UNKNOWN"
    HAVE_PERMISSION = "HAVE_PERMISSION"
    DO_NOT_HAVE_PERMISSION = "DO_NOT_HAVE_PERMISSION"
    AWAITING_REQUEST_RESPONSE = "AWAITING_REQUEST_RESPONSE"

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


class HomeScreen(Screen):
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
    pass

class WindowManager(ScreenManager):
    pass

class ScreenLoader(App):

    def build(self):

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