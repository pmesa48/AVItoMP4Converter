'''
Created on 04/04/2014

@author: pablomesa
'''

class VideoInvalidoException(Exception):
    '''
    classdocs
    '''


    def __init__(self, mensaje = '' ):
        '''
        Constructor
        '''
        self.msg = mensaje
        
    def __str__(self):
        '''
        ToString de la clase Video Invalido
        '''
        return self.msg
        
        