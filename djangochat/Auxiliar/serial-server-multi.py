#pip install pyserial
#pip install pyzmq
#pip install socketIO-client

import serial
import socket

puerto = 'COM1'  # Reemplaza 'COM1' con el puerto en el que está conectado tu dispositivo GPS
baudios = 9600  # Ajusta la velocidad de baudios según la configuración de tu dispositivo GPS
host = '0.0.0.0'  # Dirección IP del host en el que se ejecuta este código
puerto_red = 12345  # Puerto en el que se establecerá la conexión de socket

# Crear una instancia del objeto Serial para la comunicación con el dispositivo GPS
with serial.Serial(puerto, baudios, timeout=1) as ser:
    # Crear un objeto socket para la conexión de red
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Enlazar el socket a la dirección y puerto especificados
        sock.bind((host, puerto_red))
        print("Esperando conexiones en el puerto", puerto_red)
        
        # Escuchar conexiones entrantes
        sock.listen(5)  # Permite hasta 5 conexiones pendientes
        
        while True:
            # Aceptar una conexión entrante
            conn, addr = sock.accept()
            print("Conexión establecida desde", addr)
            
            # Leer datos del dispositivo GPS y enviarlos a través del socket
            while True:
                linea = ser.readline().decode('utf-8').strip()
                
                # Procesar la línea recibida del GPS
                # ...
                
                # Enviar la línea a través del socket
                conn.send(linea.encode('utf-8'))
