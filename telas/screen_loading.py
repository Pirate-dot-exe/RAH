from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar

class LoadingScreen(Screen):
    pb = ProgressBar(max=100)
    pb.value = 0

    def progressbar(self, dt):
        if self.ids.pb.value < 100:
            self.ids.pb.value += 1
            self.ids.progress_info.text = f"Loading... {int(self.ids.pb.value)}%"
            Clock.schedule_once(self.progressbar, 1/25)
        else:
            sm = ScreenManager()
            self.ids.progress_info.text = "Loading Complete! (wait a minute)"
            home = HomeScreen(name = 'home')
            sm.current = home
    
    def callback_func(self):
        Clock.schedule_once(self.progressbar, 1/25)

    def remove_myself(self):
        self.manager.remove_widget(self)