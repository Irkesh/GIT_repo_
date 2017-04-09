# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 18:36:59 2017

@author: Irkesh
"""

# Клиент игры "Запоминалка"

import socket

import gener_transaction 

HOST, PORT = 'localhost', 2102   #127.0.0.1 - localhost


class ATM(self):
 
     def __init__(self, HOST, PORT):
         self.HOST = HOST
         self.PORT = PORT
 
     def execute(self, transaction):
          sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          sock.connect((self.HOST, self.PORT))
          sock.sendall(gener_transaction.serialize())
          recvd = str(sock.recv(1024), 'utf-8')
          print(recvd)
          sock.close()

          
def main():
     if __name__ == '__main__':
         
         terminal = ATM()
         terminal.execute(gener_transaction.get_transaction())
main()
''''          
print('Клиент запущен')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

sock.sendall(bytes('I_WANNA_PLAY', 'utf-8'))

recvd = str(sock.recv(1024), 'utf-8')

print(recvd)