'''
Created on 04/04/2014

@author: pablomesa
'''
import platform
import subprocess

''' Constantes '''
FFMPEG_PATH = '/usr/local/bin/ffmpeg'
WIN_PATH = 'C:\\FFMPEG\\bin\\ffmpeg.exe'
LINUX_PATH = '/usr/bin/ffmpeg'

class Converter(object):
    '''
    classdocs
    '''
    
    def __init__(self, nombre):
        '''
        Constructor
        '''
        self.nombre = nombre
        

    def convertAVItoMP4( self, videoAVI, nameMP4 ):
        '''
        Metodo que convierte de AVI a MP4
        '''
        print 'Tipo de servidor'
        try:
            if platform.system( ) == 'Darwin':
                subprocess.call( [ FFMPEG_PATH, '-i', videoAVI.name, nameMP4 ] )
            elif platform.system( ) == 'Windows':
                print 'Servidor Windows'
                subprocess.call( [ WIN_PATH, '-i', videoAVI.name, nameMP4 ] )
            else:
                subprocess.call( [ LINUX_PATH, '-i', videoAVI.name, nameMP4 ] )
        except Exception as ex:
            print type(ex)
            print 'Problema convitiendo archivo'
            print ex
        finally:
            print 'Conversion terminada'


        