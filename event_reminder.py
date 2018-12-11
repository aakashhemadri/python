# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 10:41:25 2018
@author: Aakash Hemadri
"""
import sys
import json
from itertools import repeat

def validate_file(file):
    '''File validation.

    Create/Open File.
    '''
    try:
        with open(file,'r'):
            print('-- Opening file... \'' + file + '\'!!')
    except IOError:
        print('-- File does not exist...')
        print('-- Creating and using file \'' + file + '\'!')
        temp = []
        with open(file,'w') as fwrite:
            json.dump(temp, fwrite)

def parse_arg(arg):
    '''Parses arguments, returns a dict
    
    '''
    arg = arg[1:]
    arg = arg + list(repeat('-',(6-len(arg))))
    print(arg)
    #temp_dict = { x:y for x in ('User','Command','Date','Start','End','Description') for y in arg }
    temp_dict = dict(zip(['User','Command','Date','Start','End','Description'],arg))
    return temp_dict

def print_event(event):
    print('## [[User:' + event['User'] + ']:[Date:' + event['Date'] + ']:[Start:' + event['Start'] + ']:[End:' + event['End'] + ']:[Description:' + event['Description'] + ']]')

def process_event(event, filename = 'event_data.json'):
    '''Performs all possible operations on a user's
    
    All commands can be run as the event is unique,
    validation is done based on the events time to remove concurrency issues
    '''

    validate_file(filename)

    with open(filename,'r') as fread:
        if fread != None:
            all_events = json.load(fread)
    if event['Command'] == 'add':
        for i in range(len(all_events)):
            if(((event['Start'] >= all_events[i]['Start'] and \
                    event['Start'] < all_events[i]['End']) or \
                    (event['End'] <= all_events[i]['End'] and \
                    event['End'] > all_events[i]['Start'])) or \
                    (event['Date'] == all_events[i]['Date'] and \
                    event['User'] == all_events[i]['User'])):
                print('-- Conflict!! Event exists in the same time frame!!')
                return
        all_events.append(event)
        with open(filename,'w') as fwrite:
            json.dump(all_events, fwrite, indent = 4)
        print('-- Event added succesfully!!')
    elif event['Command'] == 'update':
        for i in range(len(all_events)):
            if(event['Date'] == all_events[i]['Date'] and \
                event['Start'] == all_events[i]['Start'] and \
                (event['End'] != all_events[i]['End'] or \
                event['Description'] != all_events[i]['Description'])):
                all_events[i] = event
            else:
                print('-- Event does not exist or No changes were made!!!')
                return
        with open(filename,'w') as fwrite:
            json.dump(all_events, fwrite, indent = 4)
        print('-- Event updated succesfully!!')
    elif event['Command'] == 'remove':
        if(event['Date'] == '-'):
            x = input('-- Are you sure that you\'d like to remove all events pertaining '
              'to the user: \'' + event['User'] + '\' (y/n)')
            if x == 'y':
                print('-- Removing events...')
                temp_events = [] # A new take on that crappy while loop
                for i in all_events:
                    if(event['User'] != i['User']):
                        temp_events.append(i)
                    else:
                        print_event(i)
                all_events = temp_events
                with open(filename,'w') as fwrite:
                    json.dump(all_events, fwrite, indent = 4)
                print('-- Removed all events pertaining to the user: \'' + event['User'] + '\'!!')
            else:
                print('-- Tata')
        elif(event['Start'] == '-'):
            i = 0
            while i < len(all_events):
                if(event['Date'] == all_events[i]['Date']):
                    print_event(all_events[i])
                    all_events.pop(i)
                    i -= 1
                i += 1
        else:
            i = 0
            while i < len(all_events):
                if(event['Date'] == all_events[i]['Date'] and event['Start'] == all_events[i]['Start']):
                    print_event(all_events[i])
                    all_events.pop(i)
                    i -= 1
                i += 1
        with open(filename,'w') as fwrite:
                json.dump(all_events, fwrite, indent = 4)
        print('-- Event(s) removed succesfully!!')
    elif event['Command'] == 'get':
        if(event['Date'] == '-'):
            print('-- Getting all events of user \'' + event['User'] +'\'')
            flag = True
            for i in all_events:
                if(event['User'] == i['User']):
                    print_event(i)
                    flag = False
            if flag == True:
                print('-- User does not exist!!')
        else:
            print('-- Printing all events pertaining to Date: ' + event['Date'] + \
                 ' and Start: ' + event['Start'] + ' ....')
            for i in range(len(all_events)):
                if event['Start'] == '-':
                    if(event['Date'] == all_events[i]['Date']):
                        print_event(all_events[i])
                elif(event['Date'] == all_events[i]['Date'] and event['Start'] == all_events[i]['Start']):
                    print_event(all_events[i])
    else:
        print('-- Invalid Command!!')

def main():
    """Begins script's execution

    Recieves arguments, and runs appropriate event_* procedure
    """
    process_event(parse_arg(list(sys.argv)))

if __name__=="__main__":
    main()