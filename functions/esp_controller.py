from functions import blt_func
import functions.socket_manager as socket_m

def controla_robo1(frame, cord_disco_x, cord_disco_y):
    socket = socket_m.conection_socket
    height, width = frame.shape[:2]
    center_x = int(width/2)
    center_y = int(height/2)
    if socket != None:
        if cord_disco_x > center_x:
            if cord_disco_y > center_y:
                blt_func.send_message(socket, 'C')
                print("RD")
            elif cord_disco_y < center_y:
                blt_func.send_message(socket, 'E')
                print("RU")
        elif cord_disco_x < center_x:
            if cord_disco_y > center_y:
                blt_func.send_message(socket, 'Z')
                print("LD")
            elif cord_disco_y < center_y:
                blt_func.send_message(socket, 'Q')
                print("LU")

        