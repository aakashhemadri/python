# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 10:41:25 2018
@author: Aakash Hemadri
"""
import sys
import json

def validate_file(file):
    try:
        with open(file,'r') as fread:
            print('Opening file... \'' + file + '\'!!')
    except IOError:
        print('File does not exist...')
        print('Creating and using file \'' + file + '\'!')
        temp = []
        with open(file,'w') as fwrite:
            json.dump(temp, fwrite)

def event_all(arg, filename = 'event_data.json'):
    '''
    Performs operations on all events of a specfic user
    Validates based on the command passed
    if either remove or get then all updates are either removed or printed
    other wise program exits
    '''
    
    validate_file(filename)

    for i in range(6):
        if len(arg)>=i:
            arg.append('-')
    user    = arg[0]
    command = arg[1]
    
    with open(filename,'r') as fread:
        all_events = json.load(fread)
    if command == 'remove':
        #print()
        x = input('Are you sure that you\'d like to remove all events pertaining '
              'to the user: \'' + user + '\' (y/n)')
        if x == 'y':
            print('Removing events...')
            temp_events = [] # A new take on that crappy while loop
            for i in all_events:
                if(user != i['User']):
                    temp_events.append(i)
                else:
                    print(i)
            all_events = temp_events
            with open(filename,'w') as fwrite:
                all_events = json.dump(all_events, fwrite, indent = 4)
            print('Removed all events pertaining to the user: \'' + user + '\'!!')
        else:
            print('Tata')
    elif command == 'get':
        print('Getting all events!!')
        flag = True
        for i in all_events:
            if(user == i['User']):
                print(i)
                flag = False
        if flag == True:
            print('User does not exist!!')
    elif (command == 'add' or command == 'update'):
        print('Add/Update is not a batch command!!')
    else:
        print('Invalid Command')

def event_unique(arg, filename = 'event_data.json'):
    '''
    All commands can be run as the event is unique,
    validation is done based on the events time to remove concurrency issues
    '''

    validate_file(filename)

    for i in range(6):
        if len(arg)>i:
            arg.append('-')
    user    = arg[0]
    command = arg[1]
    date    = arg[2]
    tstart  = arg[3]
    tend    = arg[4]
    desc    = arg[5]
    
    event =  {'User' : user, 'Date' : date, 'Start' : tstart, 'End' : tend, 'Description' : desc}
    with open(filename,'r') as fread:
        if fread != None:
            all_events = json.load(fread)
    if command == 'add':
        for i in range(len(all_events)):
            if(((event['Start'] >= all_events[i]['Start'] and \
                    event['Start'] < all_events[i]['End']) or \
                    (event['End'] <= all_events[i]['End'] and \
                    event['End'] > all_events[i]['Start'])) or \
                    (event['Date'] == all_events[i]['Date'] and \
                    event['User'] == all_events[i]['User'])):
                print('Conflict!! Event exists in the same time frame!!')
                return
        all_events.append(event)
        with open(filename,'w') as fwrite:
             all_events = json.dump(all_events, fwrite, indent = 4)
        print('Event added succesfully!!')
    elif command == 'update':
        for i in range(len(all_events)):
            if(event['Date'] == all_events[i]['Date'] and \
                event['Start'] == all_events[i]['Start'] and \
                (event['End'] != all_events[i]['End'] or \
                event['Description'] != all_events[i]['Description'])):
                all_events[i] = event
            else:
                print('Event does not exist or No changes were made!!!')
                return
        with open(filename,'w') as fwrite:
             all_events = json.dump(all_events, fwrite, indent = 4)
        print('Event updated succesfully!!')
    elif command == 'remove':
        temp = []
        if(event['Start'] == '-'):
            i = 0
            while i < len(all_events):
                if(event['Date'] == all_events[i]['Date']):
                    print(all_events[i])
                    all_events.pop(i)
                    i -= 1
                i += 1
        else:
            i = 0
            while i < len(all_events):
                if(event['Date'] == all_events[i]['Date'] and event['Start'] == all_events[i]['Start']):
                    print(all_events[i])
                    all_events.pop(i)
                    i -= 1
                i += 1
        with open(filename,'w') as fwrite:
                all_events = json.dump(all_events, fwrite, indent = 4)
        print('Event(s) removed succesfully!!')
    elif command == 'get':
        print('Printing all events pertaining to Date: ' + event['Date'] + \
              ' and Start: ' + event['Start'] + ' ....')
        for i in range(len(all_events)):
            if event['Start'] == '-':
                if(event['Date'] == all_events[i]['Date']):
                    print(all_events[i])
            elif(event['Date'] == all_events[i]['Date'] and event['Start'] == all_events[i]['Start']):
                    print(all_events[i])
    else:
        print('Invalid Command!!')

def main():
    """
    This begins script's execution
    """
    arg = list(sys.argv)
    arg = arg[1:]
    if len(arg) == 1:
        user = arg[0]
        print('No commands issued to the user',user)
    elif len(arg) <= 2:
        event_all(arg)
    elif len(arg) > 2:
        event_unique(arg)

if __name__=="__main__":
    main()