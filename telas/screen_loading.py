from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar

from telas.screen_home import HomeScreen

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
            self.go_to_home()
            self.remove_myself()
            
    def callback_func(self):
        Clock.schedule_once(self.progressbar, 1/25)

    def go_to_home(self):
        self.manager.current = "home"

    def remove_myself(self):
        self.manager.remove_widget(self)