import bluetooth        #pybluez
import subprocess
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

def try_connection(addr):
    port = 1
    passkey = "1111"
    print("ok")

    '''
    subprocess.call("kill -9 'pidof bluetooth-agent'", shell=True)
    status = subprocess.call("bluetooth-agent " + passkey + " &",shell=True)
    try:
        blt_connection = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        blt_connection.connect((addr, port))
    except bluetooth.btcommon.BluetoothError as err:
        print("cannot connect bluetooth")
        pass
        '''