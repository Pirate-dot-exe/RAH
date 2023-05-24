RAH - Robotic Air Hockey Application

---INFORMAÇÕES GERAIS---  
This Application is Using  
~Python (VE): 2.7    
~Kivy: 1.9.0  

---A FAZER---  
(*obrigatórios, +adicionais)

+solucionar o problema de no_image! na função de detecção de Aruco, assim que a camera é desligada
+implementar mais um conjunto de barras deslizantes  
+implementar try/catch para que a aplicação não crashe quando não há imagem para detecção  
+Separar a busca de bluetooth em uma thread a parte impedindo que a interface gráfica pare de responder quando existem muitos dispositivos próximos  

~~*Fazer com que sejam passados argumentos de controle do motor para o ESP32 através da detecção do disco~~  
~~+integrar a faixa de detecção ao algoritmo de rastreamento~~     
~~+integrar os dois conjuntos para estabelecer a faixa de detecção do rastreamento~~   
~~+implementar barras deslizantes~~  
~~*integrar a função de rastreamento do disco~~  
~~*integrar a função de reconhecimento dos marcadores ArUco~~  
~~*Fazer a mudança da camera para a da cv2~~     

---OBSERVAÇÕES---
O arquivo socket_manager foi criado para criar um meio acessável por todos os arquivos do socket de conexão, uma vez que sendo parte da tela de bluetooth e tendo a propriedade self, não podia ser acessável externamente