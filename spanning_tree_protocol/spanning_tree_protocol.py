#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 10:31:58 2019

@author: Aakash Hemadri
"""
import numpy

def init():
    '''Initialize graph.'''
    while True: 
        try:
            while True:
                try:
                    lan = int(input('-- Enter the number of LANs in the network topology!: ').split()[0])
                    print('-- Initializing Graph..')
                    #graph = [[0 for i in range(column)] for j in range(row)] 
                    graph = numpy.zeros((lan,lan))
                    print(graph)
                    break
                except ValueError:
                    print(ValueError)
                    print('?? Incorrect input format!.\n!! Try Again!')                
                except MemoryError:
                    print(MemoryError)
                    print('?? Not Enough Memory.\n!! Try Again with lesser number of LANs')
            print("-- Initialized!")
            print("-- Updating Graph..")
            while True:
                try:
                    n_lan = int(input("-- Enter the total number individual of connections(EDGES): ").split()[0])
                    print(n_lan)
                    break
                except ValueError:
                    print(ValueError)
                    print('?? Incorrect input format!.\n!! Try Again!')  
            print("-- Input connection relationships in this format <LAN_SPECIFIER> <LAN_SPECIFIER>: ")
            for i in range(n_lan):
                while True:
                    try:
                        x,y = map(str, input('-' + str(i + 1) + ' ').upper().split())
                        x = ord(x) - 65
                        y = ord(y) - 65
                        break
                    except(TypeError):
                        print(TypeError)
                        print("?? Expected character as input!\n!! Try Again!")
                    except ValueError:
                        print(ValueError)
                        print('?? Incorrect input format (or) input value!.\n!! Try Again!')
                    except IndexError:
                        print(IndexError)
                graph[x][y] = 1
            print(graph)
            print("-- Updated!")
            break
        except Exception as e:
            print("?? Unhandled Exception!\n!! Exiting!")
            print(e)
            return  

def graph():
    pass

def test():
    '''Test Unit'''
    init()

if __name__=='__main__':
    test()