![image](https://github.com/user-attachments/assets/aaab3463-c213-4b29-b56f-2072fce17a15)# Client-Server Python Chat

Este programa implementa un chat básico utilizando Python, basado en un modelo cliente-servidor. El sistema permite a múltiples usuarios conectarse y comunicarse en tiempo real.

## Estructura del Programa

El programa está dividido en dos archivos:

1. **server.py**: Contiene la lógica del servidor que maneja las conexiones de los clientes.
2. **client.py**: Implementa la interfaz del cliente que se conecta al servidor.

## Funcionamiento del Servidor (`server.py`)

1. **Configuración del Servidor**:
   - Se crea un socket que escucha en `localhost` (127.0.0.1) y en el puerto 9000.
   - Se inicializan listas para almacenar las conexiones de los clientes y sus apodos.

2. **Recepción de Conexiones**:
   - El servidor espera conexiones entrantes.
   - Cuando un cliente se conecta, se le pide que envíe su apodo.

3. **Manejo de Clientes**:
   - Cada cliente se maneja en un hilo separado, lo que permite que el servidor gestione múltiples conexiones al mismo tiempo.
   - Cuando se recibe un mensaje del cliente, el servidor verifica si es un mensaje de desconexión (`'SALIR'`). Si es así, notifica a los demás clientes y cierra la conexión.
   - Si el mensaje es normal, se difunde a todos los clientes conectados.

## Funcionamiento del Cliente (`client.py`)

1. **Conexión al Servidor**:
   - El cliente solicita al usuario que ingrese un apodo y se conecta al servidor.

2. **Recepción de Mensajes**:
   - En un hilo separado, el cliente recibe mensajes del servidor.
   - Si recibe el mensaje `'NICK'`, envía su apodo al servidor. Si recibe otro tipo de mensaje, lo imprime en la consola.

3. **Envío de Mensajes**:
   - En otro hilo, el cliente permite al usuario escribir mensajes.
   - Si el usuario escribe "salir", se envía el mensaje `'SALIR'` al servidor, se cierra la conexión y se termina el hilo.

## Flujo de Comunicación

- **Conexión**: El cliente se conecta al servidor y envía su apodo.
- **Intercambio de Mensajes**: Los clientes envían y reciben mensajes en tiempo real.
- **Desconexión**: Al escribir "salir", el cliente se desconecta y el servidor notifica a los demás.

## Ejecución

1. Inicia el servidor ejecutando `server.py`.
2. Inicia uno o más clientes ejecutando `client.py` en diferentes terminales.
3. Los usuarios pueden comunicarse entre sí y desconectarse escribiendo "salir".

![image](https://github.com/user-attachments/assets/6e95703f-b48a-48fb-8799-3c8bb829eef4)

