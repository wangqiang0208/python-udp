# -*- coding: utf-8 -*-
'''
Created on 2013-4-20

@author: qiangwang
'''
from socket import *
from udpthread import UdpThread
from socketlogger import getDailyLogger

if __name__ == '__main__':
    HOST = "192.168.3.101"
    PORT = 54322
    BUFFER_SIZE = 1024
    
    ADDR = (HOST, PORT)
    
    udpserver = socket(AF_INET, SOCK_DGRAM)
    udpserver.bind(ADDR)
    
    print 'udp server starting....'
    logger = getDailyLogger()
    while True:
        data = None
        addr = None
        try:
            data, addr = udpserver.recvfrom(BUFFER_SIZE)
        except:
            data = None
            addr = None
        
        if data == None or addr == None:
            continue
        udp = UdpThread(udpserver, data, addr, logger)
        udp.start()
    
    udpserver.close()
