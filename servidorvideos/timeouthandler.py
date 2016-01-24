'''
Created on 02/04/2014

@author: pablomesa
'''

import os
from datetime import datetime, timedelta

TIMEOUT = 300 #  en segundos


class TimeOutHandler(object):
    '''
    classdocs
    '''
        

    def __init__( self ):
        '''
        Constructor del handler
        '''
        self.clients = list( )
        self.allclients = list( )
        self.log = os.path.join( os.getcwd( ), 'tiempos.csv')
        self.registro = open(self.log, 'wb')
        self.registro.write( 'CLIENTE ID' + ', '+ 'ENTRADA'+', '+ 'SALIDA' +', '+ 'DURACION (s)' + ', ' + 'TAMANIO (MB)\n' )
        self.registro.close( )

    
    def addClient( self, cliente ):
        '''
        Agregar cliente a la lista
        '''
        self.clients.append( cliente )
        self.allclients.append( cliente )



    def removeClient( self, cliente ):
        '''
        Quitar cliente de la lista
        '''
        try:
                self.clients.remove( cliente )
                self.allclients.append( cliente )
        except Exception as e:
                print 'No existe el cliente %s' % cliente.id_cliente
                print e

        try:
                self.registro = open(self.log, 'ab')
                self.registro.write( cliente.id_cliente +', '+ str( cliente.date )+', '+ str( cliente.salida )+', '+ str( cliente.duracion.seconds )+ ', ' + str(cliente.tamanio)+ '\n'  )
                self.registro.close()
        except Exception as e:
                print 'Error guardando el log de clientes'
                print type(e)
                print e


    def allowClient(self, cliente):
        '''
        Verifica si se puede conectar el cliente
        '''
        for c in self.clients:
                if c.id_cliente == cliente.id_cliente and ( datetime.now() - c.date ) > timedelta( seconds = TIMEOUT ):
                        print ( datetime.now( ) - c.date )
                        return False
        return True


    def closeCSV(self):
        '''
        Cierra el archivo CSV
        '''
        self.registro.close( )
        