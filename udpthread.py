# -*- coding: utf-8 -*-
'''
Created on 2013-4-20

@author: qiangwang
'''

from threading import *
import uuid

class UdpThread(Thread):
    def __init__(self, udpserver, data, addr, logger):
        Thread.__init__(self)
        self.__server__ = udpserver
        self.__id__ = uuid.uuid4()
        self.__data__ = data
        self.__addr__ = addr
        self.__logger__ = logger
    
    def run(self):
        self.__logger__.info('server thread %s' % self.__id__)
        self.__logger__.info('work for %s:%s' % self.__addr__)
        
        while True:
            if self.__data__ != None:
                response = ('[Response] - ' + self.__data__)
                self.__server__.sendto(response, self.__addr__)
                break
        
        self.__logger__.info('complete')