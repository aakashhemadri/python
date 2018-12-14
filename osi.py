# -*- coding: utf-8 -*-
"""osi

Created on Thu Dec 13 11:43:33 2018

@author: 17pw01
"""
import socket
import time
from uuid import getnode

def create_message():
    """Return's message on users's input."""
    return str('[-- [' + time.ctime() + ']: ' + input('Enter the message you would like to send: ') + ']')

def application_layer(data):
    """Adds application layer header, returns header.
    
    Uses telnet protocol
    """
    return 'telnet' + '|' + data

def presentation_layer(data):
    """Adds presentation layer header, return header.
    
    Uses ASCII for the presentation layer
    """
    return 'ASCII' + '|' + data

def session_layer(data):
    """Session Layer.

    Session control protocol
    """
    return 'SCP' + '|' + data

def transport_layer(data):
    """Transport layer."""
    port = 9994
    return str(port) + '||' + data

def network_layer(data):
    """Network layer.
    
    """
    host_ip = socket.gethostbyname(socket.gethostname())
    dest_ip = input('Enter destination ip address: ')
    return str(host_ip) + '|' + dest_ip + '||' + data

def data_link_layer(data, parse = False):
    """Data link layer.
    
    Appends source and destination mac address
    """
    if parse == False:
        source_mac = getnode()
        source_mac = ':'.join(("%012X" % source_mac)[i:i + 2] for i in range(0, 12, 2))
        dest_mac = input("Enter the destination mac address: ")
        return str(source_mac) + '|' + dest_mac + '||' + data
    else:
        pass
def physical_layer(data, parse = False):
    """Physical layer"""
    if parse == False:
        return data
    else:
        return data

def test():
    print('%012X' % getnode())

if __name__ == '__main__':
    test()