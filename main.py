#support
#s://github.com/inclement/colour-blind-camera/blob/master/camera2/main.pyhttp

import sys
sys.path.append('telas')

import kivy 
kivy.require('1.9.1')
from kivy.app import App
from kivy.lang import Builder
#Gerenciamento Multi-Telas / MultiScreen Management
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
#Exibição de Imagens / Images Exibition
from kivy.uix.image import Image


Builder.load_file('telas/loading_screen.kv')
Builder.load_file('telas/home_screen.kv')
Builder.load_file('telas/bluetooth_screen.kv')
Builder.load_file('telas/camera_screen.kv')

import rah_permissions
from telas.screen_loading import LoadingScreen
from telas.screen_home import HomeScreen
from telas.screen_camera import CameraScreen
from telas.screen_bluetooth import BluetoothScreen

class WindowManager(ScreenManager):
    pass

class ScreenLoader(App):

    def build(self):
        rah_permissions.ask_permission()

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