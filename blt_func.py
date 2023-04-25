#TODO: 
#Implementar função que permita o envio de dados ao dispositivo

import bluetooth        #pybluez, talvez funcione apenas no win

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
    import socket

    ports = range(1, 30)  # Números de porta a serem verificados
    for port in ports:
        print("trying to connect at port" + str(port) + "...")
        sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        try:
            sock.connect((addr, port))
            print("Conexao estabelecida com sucesso!")
            return sock
        except socket.error as err:
            print("nao foi possivel se conectar a porta ", port)
    return None

#Uncomment this line to direct test of try_connection function
#try_connection("84:CC:A8:7A:06:7A")

def send_data(socket):
    #implement send_data
    pass