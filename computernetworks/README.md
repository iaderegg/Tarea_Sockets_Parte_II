# explicación teórica de el programa socket-05.py

Este programa crea un socket tipo IPv4 el cual se conecta posteriormente a un servidor en la dirección ip 
la cual se obtiene con base en un nombre de host (ej. "campusvirtual.univalle.edu.co")
y un puerto el cual se especifica en la variable creada "port" Una vez establecida la conexión se envía una petición la cual esta almacenada en la variable "message"
e indica una petición por el protocolo http, una vez enviada esta petición, el servidor escribe en el socket 
la información referente a la pagina  y por ultimo el programa imprime el html de dicha página
por consola.
