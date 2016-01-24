'''
Created on 02/04/2014

@author: pablomesa
'''

import threading
import os
from cliente import Cliente
from converter import Converter
from datetime import datetime

'''
Constantes
'''
IDCLIENTE = 'CLIENTE'
LISTO = 'LISTO'
SEND_VIDEO = 'Video Send'
FIN = '\n\r\n\r'
CLOSECONNECTION = "Close Connection"
PORT = 10123
BYTELEN = 1024

class ComunicacionCliente(threading.Thread):
    '''
    classdocs
    '''


    def __init__( self, socket, numeroThread, timeout ):
        '''
        Constructor
        '''
        threading.Thread.__init__( self )
        self.connection = socket
        self.numero = numeroThread
        self.timeout = timeout
        
    def run(self):
        '''
        metodo principal del thread
        '''
        print 'Thread numero %s atendiendo' % str( self.numero )
        connection = self.socket
        data = connection.read( BYTELEN )
        print data
        data, id_client = data.split( '#' )
        print id_client
        cliente = Cliente( self.ip, datetime.now( ) )
        allow = self.timeout.allowClient( cliente )
        direccioni = self.ip.replace(".","_")
        if allow:
                print 'Cliente valido con id %s' % cliente.id_cliente
                self.timeout.addClient( cliente )
                print 'Cliente agregado al sistema'
                video = ''
                chunk = 0
                if data == IDCLIENTE:
                        f = open( 'video_' + direccioni + '-' + str( self.i ) + '.avi', 'wb' )
                        self.socket.send( LISTO )
                        print 'Servidor LISTO'
                        data = connection.read( BYTELEN )
                        video = data
                        print 'Recibiendo video ...'
                        while data:
                                if chunk % 2000 == 0:
                                        print 'chunk ' + str(chunk)
                                chunk += 1
                                video += data
                                data = connection.read( BYTELEN )
                                
                                if SEND_VIDEO in data :
                                        data = data[ 0 : len( data ) - len( SEND_VIDEO ) ]
                                        video += data
                                        print 'Video recibido'
                                        break

                        if chunk > 0 and data != IDCLIENTE:
                                f.write( video )
                                f.close()
                                print 'Video escrito'
                                cliente.modificarTamanioVideo( f )
                                #connection.send(VIDEO_COMPLETED)
                                direccion = os.path.join( os.getcwd( ) , 'video_' + direccioni + '-' + str(self.i) + '.mp4')

                                #Comenzar a convertir el video a AVI
                                print 'Comenzando a convertir'
                                connection.write( FIN )
                                c = Converter( 'AVItoMP4' )
                                c.convertAVItoMP4( f,direccion )
                                #AQUI ESTA EL ERROR
                                print direccion 
                                t = open( direccion, 'rb' )
                                envio = t.read( BYTELEN  )
                                while envio:
                                        try:
                                                connection.write( envio )
                                                envio = t.read( BYTELEN )
                                        except Exception as e:
                                                print type(e)
                                                print e
                                                break
                                connection.write( FIN )
                                data = connection.read( BYTELEN )
                                if data == CLOSECONNECTION:
                                        cliente.registrarSalida( datetime.now( ) )
                                        self.timeout.removeClient( cliente )
                                        print 'Cerrar conexion con cliente %s ' % self.ip
                                        connection.close( )
        else:
                print 'Servicio denegado a %s por posible ddos' % self.ip
                connection.close()
        
        
         
        
    
        