'''
Created on 02/04/2014

@author: pablomesa
'''
import socket
import ssl

from comunicacion import ComunicacionCliente
from timeouthandler import TimeOutHandler

'''Constantes'''
IDCLIENTE = 'CLIENTE'
LISTO = 'LISTO'
SEND_VIDEO = 'Video Send'
FIN = 'FIN'
CLOSECONNECTION = "Close Connection"
BYTELEN = 1024
CLIENTNUMBER = 300


'''Variables'''
i = 0
threads = list( )
clients = list( )
serversock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
serversock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )

class Servidor(object):
    '''
    Servidor de conversion de videos
    '''
    server_address = None


    def __init__(self, address, port):
        '''
        Constructor
        '''
        self.server_address = ( address, port )
        serversock.bind( self.server_address )
        self.timeout = TimeOutHandler( )
        
    
    def main(self):
        '''
        Metodo principal que espera conexiones de clientes
        '''
        while True:
            try:
                serversock.listen( CLIENTNUMBER )
                clientsock, client_address = serversock.accept()
                connection = ssl.wrap_socket(clientsock, server_side=True,keyfile="CA/key.pem", certfile="CA/certificado-pato.pem", do_handshake_on_connect=True, ciphers="RSA", ssl_version=ssl.PROTOCOL_SSLv23) 
                client = ComunicacionCliente( self.server_address, connection, i, self.timeout )
                client.start( )
                print 'Cliente %s conectedo usando puerto %s' % client_address 
                threads.append( client )
                i += 1
            except Exception as error:
                print type( error )
                print error
                print 'Error in connection with %s' % client_address[ 0 ]
                connection.close( )
                threads.remove( client )
                
        
        
        
        
        