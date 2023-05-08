from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.utils import platform

class BluetoothScreen(Screen):
    import functions.blt_func as blt

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
            else:
                pass
        elif platform=='android':
            self.ids.devices_found.text = "Sorry, no implemented yet :p"
                    
    def try_connection(self, addr):
        print("try_connection")
        self.connection_socket = self.blt.try_connection(addr)
        if self.connection_socket is not None:
            self.ids.connected_bluetooth.text = "Device connected"
            self.ids.blt_send_data.disabled = False
            self.disconnect_button = Button(
                text="disconnect device",
                on_press=(
                    lambda x: self.close_connection(self.connection_socket)
                )
            )
            self.ids.connection_layout.add_widget(self.disconnect_button)
        else:
            pass
    
    def close_connection(self, socket):
        self.blt.close_connection(socket)
        self.ids.connection_layout.remove_widget(self.disconnect_button)
        self.ids.blt_send_data.disabled = True
        self.ids.connected_bluetooth.text = "No connected Devices!"

    def send_message(self):
        message = self.ids.blt_message.text
        self.blt.send_message(self.connection_socket, message)