'''
Created on Oct 9, 2018

@author: Angelina
'''
import files
from events import Event
from Items import Item

def main():
    #creates a boolean variable
    keep_going=True
    #loops through this main function while the boolean is true (allows the user to repeatedly make new choices) until they choose to exit
    while keep_going == True:
        print("Welcome to the expenses program")
        #gets the choice from the user
        choice=choose_action()
        
        #checks the users choice, and runs matching code
        if choice =="E":
            #attempts to get the user to choose an event, and allows the user to work with that event
            try:
                chosen_event=choose_event()
                event_action(chosen_event)
            except:
                pass
        if choice == "P":
            #prints all the info
            print_events()
        elif choice == "T":
            #calculates the total cost
            get_total_cost()
        elif choice == "A":
            #adds an event to the program
            add_event()
        elif choice == "R":
            #removes an event from the program. Must get the name of the removed event first.
            removed=input("What is the name of the event you would like to remove?")
            files.remove_from_file(removed)
        elif choice == "Q":
            #sets boolean to false and allows the program to stop running
            print("Thank you for running the expenses program")
            keep_going = False
    
def choose_event():
    '''
    function that gets the users choice for the event they want to run
    displays the events, and then checks if the user's choice is available
    returns the user's choice
    '''
    f=open("event_names.txt")
    #reads all the lines from the file, sets it to a variable list
    list_of_events=f.readlines()
    f.close()
    
    #prints out the name of all the events
    print("The events you can choose are:")
    print(list_of_events)
    
    #gets the users input for their choice, formats it appropriately 
    choice=input("What event would you like to change/edit/view?").strip().lower()
    
   
    #loops through all the lines in the file list, checking if the users choice is available, and then returns that choice, else prints an error message
    for event in list_of_events:
        #replaces all the newlines in the list to better compare to the users choice
        event=event.replace("\n","")
        
        #compares the name of the event in the list to the user's choice
        if choice == event:
            return choice
        elif choice != event:
            print("Sorry, that event isn't added yet")
        
        
def event_action(event):
    '''
    asks the user what they want to do with the chosen event
    then runs appropriate code based on their choice
    returns nothing
    '''
    
    #allows the user to choose an action
    choice=input("What would you like to do? Enter [L] to change the leader, [A] to add an item," \
                  "\n [R] to remove an item, [P] to print the event, [CN] to change the name of an item, [CP] to change the price of an item, [T] to view the total cost.").upper()
    #makes sure the users choice has to be one of the available options, and repeats asking until their choice fits
    while choice not in ("A","L","R","P","CN","CP", "T"):
        print("Invalid choice")
        choice=input("What would you like to do? Enter [L] to change the leader, [A] to add an item," \
                      "\n[R] to remove an item, [P] to print the event,[CN] to change the name of an item, [CP] to change the price of an item, [T] to view the total cost.").upper()
    #loads the chosen event from its file, and sets it to a new Event object
    event2=files.load_file(event)
    
    #if the event couldn't be retrieved, prints an error message and exits the function
    if event2 == "error":
        print("Couldn't open the file")
        
    
    #runs code based on the users choice
    if choice=="A":
        #adds an item to the event
        event2.add_items()
    elif choice == "R":
        #removes an item from the event
        event2.remove_item()
    elif choice=="L":
        #gets the users choice for a new leader, then changes it to that choice
        leader=input("What is the name of the new leader?")
        event2.change_leader(leader)
    elif choice=="P":
        #prints all the Items in the event
        print (event2)
    elif choice =="CN":
        #sets a boolean to false
        found = False
        
        #creates the name of the item
        og_name=input("What's the item you wish to change the name of?").strip().lower()
        #checks all the available items in the event
        for item in event2.items:
            #if the wanted name is found, runs the change_name function, sets the boolean to true, and exits from the loop
            if og_name == item.title:
                item.change_name()
                found=True
                break
        #if the wanted item is never found, prints an error message and exits the function
        if found==False:
            print("Couldn't find that item")
            
    elif choice == "CP":
        #sets a boolean to false
        found=False
        
        #creates the name of the item
        og_name=input("What's the item you wish to change the price of?").strip().lower()
        #checks all the available items in the event
        for item in event2.items:
            #if the wanted name is found, runs the change_price function, sets the boolean to true, and exits from the function
            if og_name == item.title:
                item.change_price()
                found=True
                break
        #if the wanted item is never found, prints an error message and exits the function
        if found == False:
            print("Couldn't find that item")
    elif choice == "T":
        #gets the total from the objects function
        total=event2.total_cost()
        #prints a formatted statement displaying the cost
        print("The total cost of this station is $ {}".format(total))
    
    #saves all the changes made back to the file
    files.save_to_file(event2.items,event2.name)       
    
    
        
def choose_action():
    '''
    gets input from the user, asking what they would like to do.
    Runs through a loop to make sure their choice is one of the available ones
    returns the user's input
    '''
    #gets the users input
    action=input("What would you like to do? [E] to access an event, [P] to print all events, [T] to get the total from all events," \
            "\n [A] to add an event, [R] to remove an event,[Q] to exit").upper().strip()
    #checks if the entered input is within the list of wanted input
    while action not in ("E","P","T","A","R","Q"):
        print("Sorry, not valid choice, try again")
        action=input("What would you like to do? [E] to access an event, [P] to print all events, [T] to get the total from all events," \
            "\n [A] to add an event, [R] to remove an event").upper().strip()
            
    #returns user's input
    return str(action)
def print_events():
    '''
    prints all of the events on file
    opens a file containing the names of all the events, and creates a list containing all the names
    creates event objects for every event
    prints all of the events
    returns nothing
    '''
    f=open("event_names.txt")
    #creates a list from the file
    list_of_events=f.readlines()
    f.close()
    
    #goes through every event name in the list
    for event in list_of_events:
        #replaces the newline character in every event name
        event=event.replace("\n","")
        #creates an Event object by loading the file for every available event
        events=files.load_file(event)
        #breaks from the loop if an error appears
        if events == "error":
            break
        #prints the event
        print(events.name)
        print(events)
        
        #for formatting, makes it look nice after printing
        print("*"*15+"\n")
    
def get_total_cost():
    '''
    opens a list of all the events, creates Event objects by loading their files, and calculates the total costs of each event
    calculates a grand total by adding all the total costs
    returns nothing
    '''
    f=open("event_names.txt")
    #creates a list from the file
    list_of_events=f.readlines()
    f.close()
    grand_total=0
    
    #goes through every event in the list of events
    for event in list_of_events:
        #replaces the newline in every event name
        event=event.replace("\n","")
        #creates an event object by loading their file
        events=files.load_file(event)
        #adds the total cost of each event to the grand total, as a float value
        grand_total+=float(events.total_cost())
        
    #prints the grand total   
    print("Grand total: ${}".format(grand_total))
    
    
def add_event():
    '''
    creates a new event object
    saves that event to a file
    '''
    #initializes a new Event object
    new_event=Event()
    #saves it
    files.save_to_file(new_event.items,new_event.name)
    
#runs the program
if __name__=="__main__":
    main()

    