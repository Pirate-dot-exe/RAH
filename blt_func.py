#TODO: 
#Implementar/Adaptar função que faça o pareamento com o dispositivo escolhido 
#Implementar função que permita o envio de dados ao dispositivo

import bluetooth        #pybluez, talvez funcione apenas no win
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
        find_services(addr, name)
    return nearby_devices, device_list

def find_services(addr, name):
    services = bluetooth.find_service(addr)
    if len(services) <= 0:
        print("no services found for "+ name)
    else: 
        for serv in services:
            print(serv['name'])

def try_connection(addr):
    port = 4
    passkey = "1111"
    print("trying blt connection to " + addr)

    subprocess.call("kill -9 'pidof bluetooth-agent'", shell=True)
    status = subprocess.call("bluetooth-agent " + passkey + " &",shell=True)
    try:
        blt_connection = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        blt_connection.connect((addr, port))
    except bluetooth.btcommon.BluetoothError as err:
        print("cannot connect bluetooth")
        pass
#testes---------------------------------------------------------------------------------------------------
def try_connection_socket(addr):
    import socket

    ports = range(1, 30)  # Números de porta a serem verificados
    for port in ports:
        print("trying to connect at port" + str(port) + "...")
        sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        try:
            sock.connect((addr, port))
            print("Conexão estabelecida com sucesso!")
            break
        except socket.error as err:
            print("nao foi possivel se conectar a porta ", port)
        sock.close()
#try_connection_socket(val_esp)