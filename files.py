'''
Created on Oct 10, 2018

@author: Angelina
'''
#all the imports required for this file
from Items import Item
import json
import os
from events import Event
def save_to_file(items,event_name):
    '''
    takes a list of items and the name of the event
    converts that list to a dictionary
    saves that to the proper json file, named after the event
    also makes a file that has a saved list of all the events
    also opens a file containing the name of all the events, and adds to it if the passed event doesn't exist in the file already
    returns nothing
    '''
    #makes a new directory
    try:
        os.mkdir("events")
    except:
        pass
    
    dict_items={}
    #opens file from current directory matching the name of the event
    f=open("events/"+event_name+".json", "w+")
    #creates a dictionary from the items in the list
    for i in range(len(items)):
        key=items[i].title
        value=items[i].price
        #adds a new dictionary item to the dictionary
        dict_items[key]=value
    #adds that dictionary to the json file (overwrites file)
    json.dump(dict_items,f,indent=2)
    f.close()
    
    f=open("event_names.txt")
    #copies content of file to a list
    events=f.readlines()
    f.close
    
    #overwrites the file, prepares it for writing
    f=open("event_names.txt", "w+")
    
    #checks if the event already exists, and if it doesn't, adds it to the list
    #includes newline in order to be consistent with how files are written
    if (event_name+"\n") not in events:
        events.append(event_name+"\n")
        print("Event successfully saved")
    
    #writes the list into the file    
    f.writelines(events)
    f.close()
        
    
def load_file(event_name):
    '''
    takes the name of an event, and opens a json file that matches that name
    converts the dictionary of the file to a list, using the Item object
    creates an Event object from the file
    return that Event object
    '''
    #attempts to open the wanted file
    try:
        f=open("events/"+event_name+".json")
    except:
        print("Sorry, couldn't find file")
        return "error"
    
    #loads the file into a dictionary
    dict_items=json.load(f)
    f.close()

    items=[]
    #loops through the loaded dictionary. Assigns every key to the name of an item object and every value of that key to the price of an item object
    #creates a list of Item objects, adding to it in each loop
    for key in dict_items:
        loaded_item=Item(title=key,price=dict_items[key])
        items.append(loaded_item)
        
    #creates an event object using the given name and list of items created above
    this_event=Event(name=event_name,items=items)
        
    #returns the event
    return this_event

def remove_from_file(event_name):
    '''
    Takes the name of an event, and removes it from the program.
    Starts by removing it from the list of events file, and then deletes the file that contains its information
    '''
    f=open("event_names.txt")
    #creates a list from the contents of the file
    events=f.readlines()
    f.close()
    
    #checks if the event exists in the file (from the list). If it does, it gets removed from the list and the file is rewritten, otherwise prints an error message
    #includes newline character in order to be consistent with how files are written and read (they must be acconuted for)
    if (event_name+"\n") in events:
        events.remove(event_name+"\n")
        f=open("event_names.txt","w+")
        #rewrites file with updated list
        f.writelines(events)
        f.close()
    else:
        print("Couldn't find that event")
        
    #checks if the file for the event exists. If it does, then that file is deleted. Prints an error message otherwise
    if os.path.exists("events/"+event_name+".json"):
        os.remove("events/"+event_name+".json")
    else:
        print("The file does not exist")
        