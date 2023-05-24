import cv2
import numpy as np

from functions import esp_controller

def find_disk(ret, frame):
    
    # Convertendo o frame para o espaço de cor HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Definindo os limites inferiores e superiores da cor vermelha
    lower_red = np.array([0, 150, 75])
    upper_red = np.array([10, 255, 200])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170, 150, 75])
    upper_red = np.array([180, 255, 200])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    # Combinando as duas máscaras para obter a máscara final
    mask = cv2.bitwise_or(mask1, mask2)

    # Aplicando a operação de abertura na máscara para remover ruídos
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Encontrando os contornos dos objetos na máscara
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # Encontra o centro do objeto
        moments = cv2.moments(contour)
        if moments["m00"] != 0:
            cx = int(moments["m10"] / moments["m00"])
            cy = int(moments["m01"] / moments["m00"])

            # Desenha a cruz azul no centro do objeto
            size = 20
            thickness = 2
            color = (255, 0, 0) # cor azul (BGR)
            cv2.drawMarker(frame, (cx, cy), color, cv2.MARKER_CROSS, size, thickness)

            esp_controller.controla_robo1(frame,cx,cy)
        
    #get_setor(frame)

    return frame


#função de suporte, apenas define a imagem em 4 quadrantes
def get_setor(frame):
    height, width = frame.shape[:2]

    center_x = int(width/2)
    center_y = int(height/2)
    start_x_point = (center_x, 0)
    end_x_point = (center_x, height)
    start_y_point = (0, center_y)
    end_y_point = (width, center_y)

    line_color = (10, 255, 10)
    espessura = 2
    cv2.line(frame, start_x_point, end_x_point, line_color, espessura)
    cv2.line(frame, start_y_point, end_y_point, line_color, espessura)

    return frame