#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""OSI model representationc

Created on Wed Dec 12 11:05:47 2018

@author: Aakash Hemadri
"""
import sys
import socket
import time

def create_message():
    """Return's message on users's input."""
    return str('-- [' + time.ctime() + ']: ' + input('Enter the message you would like to send: '))

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
    """

    Session control protocol
    """
    return 'SCP' + '|' + data

def transport_layer(data):
    """Transport layer"""
    return 'UDP' + '|' + data

def network_layer(data):
    """Network layer,

    """
    return 'IPv4' + '|' + data

def data_link_layer(data):
    """Data link layer,

    """
    return data

def physical_layer(data):
    """Physical layer,

    """
    return data

def main():
    """Begins script's execution
    
    """
    print(physical_layer(data_link_layer(network_layer(transport_layer(application_layer(create_message()))))))

if __name__=='__main__':
    main()
