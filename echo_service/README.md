#Echo Service

En este directorio se encuentran dos archivos, a continuación se explica que hace cada uno.

##1. echo-client.py 
En el archivo echo-client.py se programa un cliente de tipo echo, en el cual, al conectarse al servidor, este le devolverá lo mismo que el envia.

Para ejecutar este archivo es necesario escribir el siguiente comando: python echo-client.py --port=12000
donde  el valor 12000 es el puerto donde espera que el servidor le escuche.

##2. echo-server.py
En el archivo echo-server.py se programa un sevidor de tipo echo, el cual regresará al cliente lo que el le envie.

Para ejecutar este archivo es necesario escribir el siguiente comando: python echo-server.py --port=12000
donde el valor 12000 es el puerto donde escuchará al cliente que se conecte.
