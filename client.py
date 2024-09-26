import socket
import threading

apodo = input('Ingresa tu apodo: ')

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('127.0.0.1', 9000))

def recibir_mensajes():
    while True:
        try:
            mensaje = cliente.recv(1024).decode('utf-8')
            if mensaje == 'NICK':
                cliente.send(apodo.encode('utf-8'))
            else:
                print(mensaje)
        except:
            print('Se ha producido un error.')
            cliente.close()
            break

def enviar_mensajes():
    while True:
        mensaje = f'{apodo}: {input("")}'
        if mensaje.lower() == f'{apodo}: salir':
            cliente.send('SALIR'.encode('utf-8'))
            cliente.close()
            break
        cliente.send(mensaje.encode('utf-8'))

hilo_recibir = threading.Thread(target=recibir_mensajes)
hilo_recibir.start()

hilo_enviar = threading.Thread(target=enviar_mensajes)
hilo_enviar.start()
