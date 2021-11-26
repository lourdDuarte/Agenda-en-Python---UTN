import socket
import threading
import socketserver
from pathlib import Path
import os
import sys
import binascii
from datetime import datetime
import time

#global HOST
global PORT



class MyUDPHandler(socketserver.BaseRequestHandler):


    def handle(self):
        log = open("server_registro.log", "a")
        data = self.request[0].strip()
        socket = self.request[1]
   
        binary_field = bytearray(data)
        print("Valor recibido: ", binascii.hexlify(binary_field).decode("utf-8"))
        mi_string = binascii.hexlify(binary_field).decode("utf-8")
        if mi_string == '00003ef5':
            print("se actualizo un registro")
            log.write(time.strftime("%d/%m/%y") + " " + time.strftime("%H:%M:%S") + " : " + "se actualizo un registro\n")
        elif mi_string == '00003ef8':
            print(time.strftime("%d/%m/%y") + " " + time.strftime("%H:%M:%S") + " : " + "se inserto un nuevo registro\n")
            log.write("se inserto un nuevo registro")
        elif mi_string == '00003ef3':
            print("se elimino un registro")
            log.write(time.strftime("%d/%m/%y") + " " + time.strftime("%H:%M:%S") + " : " + "se elimino un registro\n")
        # ####################################################
        #   Paquete e
        # ####################################################

        value2 = 0xA0
        packed_data_2 = bytearray()
        packed_data_2 += value2.to_bytes(1, "big")
        socket.sendto(packed_data_2, self.client_address)
        log.close()

        
if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 55555
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        print('server corriendo en el host: {}, port: {}'.format(HOST,PORT))
        server.serve_forever()
        
