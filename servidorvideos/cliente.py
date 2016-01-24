'''
Created on 04/04/2014

@author: pablomesa
'''
import os
from datetime import datetime

class Cliente(object):
    '''
    classdocs
    '''


    def __init__(self, address, idnum, tiempo_llegada):
        '''
        Constructor
        '''
        self.address
        self.id = idnum
        self.tiempo_llegada = tiempo_llegada
        self.tamanio_video = 0
        
    def darTiempoEnConexion(self):
        ahora = datetime.now()
        return ( ahora - self.tiempo_llegada ).seconds
    
    def modificartamanio_video(self, video):
        tamanioBytes = os.path.getsize( video )
        self.tamanio_video = tamanioBytes / ( 1024 ** 2 )
        
    def darIDCliente(self):
        return self.address.replace( '.','-' ) + '--' + self.id
        
        