import socket

host = '192.168.0.128'  # Reemplaza '192.168.0.100' con la dirección IP del host que ejecuta el código de envío
puerto_red = 12345  # Puerto en el que se estableció la conexión de socket

# Crear un objeto socket para la conexión de red
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Conectar al host y puerto especificados
    sock.connect((host, puerto_red))
    print("Conectado al servidor", host)
    
    # Recibir y procesar los datos del GPS
    while True:
        datos = sock.recv(1024).decode('utf-8')
        
        # Procesar los datos recibidos
        # ...
        
        print(datos)  # Imprimir los datos para fines de demostración
