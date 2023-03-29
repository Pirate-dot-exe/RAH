import bluetooth        #pybluez
import time

def search_new_devices():
    device_list = ''
    nearby_devices = bluetooth.discover_devices(
        duration = 5,
        lookup_names=True
    )
    print("Devices found!")
    for addr, name in nearby_devices:
        print("address: ", addr, "name: ", name)
        device_list = device_list + "name: " + name + " address: " + addr + "\n"

    return nearby_devices, device_list