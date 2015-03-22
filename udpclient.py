# -*- coding: utf-8 -*-
'''
Created on 2013-4-20

@author: qiangwang
'''
from socket import *
import uuid
from threading import Thread
import random
import time

def connection(name, host, port):
    count = 0
    rnd = random.Random()
    while count < 10:
        addr = (host, port)
        size = 1024
        udpclient = socket(AF_INET, SOCK_DGRAM)
        udpclient.sendto('%s send %d' % (name, count), addr)
        data, addr = udpclient.recvfrom(size)
        if data != None:
            print data
        
        count = count + 1
        
        udpclient.close();
        time.sleep(2 / rnd.randint(1, 50))
    
if __name__ == '__main__':
    
    HOST = '192.168.3.103'
    PORT = 54322
    
    for i in range(0, 5):
        name = uuid.uuid4().time_mid
        t = Thread(target = connection, args = (name, HOST, PORT))
        t.start()