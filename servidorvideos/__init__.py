import os
import sys
import platform
from servidor import *

SERVER_ADDRESS = 'localhost'
SERVER_PORT = 10001

def main():
    print "Servidor iniciado"
    servidor = Servidor( SERVER_ADDRESS, SERVER_PORT )
    servidor.main()

if __name__ == "__main__":
    main()
    