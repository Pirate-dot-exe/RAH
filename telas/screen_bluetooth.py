from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.utils import platform

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