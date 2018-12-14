# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 11:18:25 2018

@author: 17pw01
"""

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9994
s.connect((host,port))
message = s.recv(1024)
s.close

print(message)