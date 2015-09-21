#/usr/bin/python
import socket
import sys
from thread import *

HOST = '' # Este servidor escuchara por todas las interfaces de red
PORT = 8888 # Un identificador de puerto cualquiera

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		# Crea un socket 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print 'Socket created'

try:
	s.bind((HOST, PORT)) # Esta funcion asocia un socket a un IP y un port
except socket.error, msg:
	print 'Bind failed. Error code: ' + str(msg[0]) + ' message ' + msg[1]
	sys.exit()

print 'Socket bind complete'

s.listen(10)
print 'Socket now listening'

# Funcion que maneja las conexiones. Puede ser usada para crear hilos.
def clientthread(conn):
	# Mandando un  mensaje a un cliente conectado
	conn.send('Bienvenido al servidor. Escriba algo y presione Enter\n')
	
	# Ciclo infinito para que la funcion y el hilo no terminen
	while True:
		# Recibiendo datos del cliente
		data = conn.recv(1024)
		reply = 'OK...' + data
		if not data :
			break
		conn.sendall(reply)
	
	# Al salir del ciclo
	conn.close()
	
# Hablando con el cliente
while 1:
	# Esperando para aceptar la conexion
	conn, addr = s.accept()
	print 'Conectado con: ' + addr[0] + ':' + str(addr[1])
	
	# Empieza un nuevo hilo: Toma como primer argumento la funcion que se ejecutara
	# y como segundo argumento la tupla de los argumentos de dicha funcion
	start_new_thread(clientthread, (conn,))
	
# Cerrando el socket
s.close()


# Vaya a la pagina 
# http://www.binarytides.com/python-socket-programming-tutorial/
# pretende hacer esta nueva parte del codigo. Adicionelo a este programa

