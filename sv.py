#sv - #SERVER

from socket import *

address = "LOCALHOST"
port = 9099

#Parametros conexion TCP - sin perdida
sck_server = socket(AF_INET, SOCK_STREAM)

sck_server.bind(address,port)


while True:
	pass
	