import requests
import socket

url_gps = 'http://192.168.0.20:8003'  # Reemplaza con la dirección IP y puerto del servidor GPS
host = '192.168.0.128'  # Dirección IP del host en el que se ejecuta este código
puerto_red = 12345  # Puerto en el que se establecerá la conexión de socket

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
        
        # Leer datos del servidor GPS y enviarlos a través del socket
        while True:
            try:
                # Realizar una solicitud GET al servidor GPS
                response = requests.get(url_gps)
                
                # Obtener los datos de respuesta
                datos = response.text
                print(datos)
                # Procesar los datos recibidos del servidor GPS
                # ...
                
                # Enviar los datos a través del socket
                conn.send(datos.encode('utf-8'))
                
            except requests.exceptions.RequestException as e:
                print('Error en la solicitud:', e)
                break

# import socket

# host = '192.168.0.20'  # Dirección IP del servidor que proporciona los datos del GPS
# puerto = 8003  # Puerto en el que se establece la conexión de socket

# # Crear un objeto socket para la conexión de red
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#     # Conectar al servidor en la dirección y puerto especificados
#     sock.connect((host, puerto))
#     print("Conectado al servidor", host)
    
#     # Recibir y mostrar los datos del GPS en la consola
#     while True:
#         datos = sock.recv(1024).decode('utf-8')
#         print(datos)
# Esperando conexiones en el puerto 12345
# Conexión establecida desde ('192.168.0.176', 49908)
# Error en la solicitud: ('Connection aborted.', BadStatusLine('162055,3801.9666,S,05731.9161,W,1,7,2.6,14,M,11,M,,\r\n'))
# Conexión establecida desde ('192.168.0.176', 49909)
# Error en la solicitud: ('Connection aborted.', BadStatusLine('$GPGLL,3801.9664,S,05731.9162,W,162105,A\r\n'))
# Conexión establecida desde ('192.168.0.176', 49910)
# Error en la solicitud: ('Connection aborted.', BadStatusLine('$GPGLL,3801.9663,S,05731.9163,W,162115,A\r\n'))
# Conexión establecida desde ('192.168.0.176', 49913)
# Error en la solicitud: HTTPConnectionPool(host='192.168.0.20', port=8003): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x00000216ADC77820>: Failed to establish a new connection: [WinError 10061] No se puede establecer una conexión ya que el equipo de destino denegó expresamente dicha conexión'))