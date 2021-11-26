import socket
import sys
import binascii

class cliente:
    def __init__(self, HOST = "127.0.0.1", PORT=55555):
        self.HOST, self.PORT = HOST,PORT
        self.data = " ".join(sys.argv[1:])
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # ################################################333

    def message(self,mi_valor):
        #mi_valor = 0x00003EF5
        print(type(mi_valor))
        packed_data = bytearray()
        packed_data += mi_valor.to_bytes(4, "big")
        mensaje = packed_data
        self.send_message(mensaje)


    def send_message(self,mensaje):
        self.sock.sendto(mensaje, (self.HOST, self.PORT))
        received = self.sock.recvfrom(1024)
        # ===== ENVIO Y RECEPCIÓN DE DATOS =================
        print(binascii.hexlify(mensaje).decode("utf-8"))
        print("Sent:     {}".format(self.data))
        print("Received: {}".format(received))
        print(binascii.hexlify(received[0]).decode("utf-8"))
        # ===== FIN ENVIO Y RECEPCIÓN DE DATOS =================

