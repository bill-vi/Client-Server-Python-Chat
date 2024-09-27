import socket
import threading

HOST = '127.0.0.1'
PORT = 9000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()

clientes = []
apodos = []

def difundir(mensaje):
    for cliente in clientes:
        cliente.send(mensaje)

def manejar_cliente(cliente):
    while True:
        try:
            mensaje = cliente.recv(1024)
            if mensaje.decode('utf-8') == 'SALIR':
                index = clientes.index(cliente)
                apodo = apodos[index]
                difundir(f'{apodo} se ha desconectado.'.encode('utf-8'))
                clientes.remove(cliente)
                apodos.remove(apodo)
                cliente.close()
                break
            else:
                difundir(mensaje)
        except:
            index = clientes.index(cliente)
            apodo = apodos[index]
            difundir(f'{apodo} se ha desconectado.'.encode('utf-8'))
            clientes.remove(cliente)
            apodos.remove(apodo)
            cliente.close()
            break

def recibir_conexiones():
    while True:
        cliente, direccion = servidor.accept()
        print(f'Conectado con {str(direccion)}')

        cliente.send('NICK'.encode('utf-8'))
        apodo = cliente.recv(1024).decode('utf-8')
        apodos.append(apodo)
        clientes.append(cliente)

        print(f'Apodo del cliente: {apodo}')
        difundir(f'{apodo} se ha unido al chat.'.encode('utf-8'))
        cliente.send('Conectado al servidor.'.encode('utf-8'))

        hilo = threading.Thread(target=manejar_cliente, args=(cliente,))
        hilo.start()

print("El servidor está escuchando...")
recibir_conexiones()
