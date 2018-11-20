'''
Created on Oct 9, 2018

@author: Angelina

'''
from Items import Item
class Event(object):
    
    '''
    Event object
    has the properties of a name, a leader, and items that the event has (using the Item object before)
    '''
    #initializes class attributes 
    def __init__(self,name="",leader="",items=[]):
        '''
        initiates all the variables, make sure they're present and proper
        '''
        
        self.name=name.strip().lower()
        #gets a name attribute if not given, formats it properly 
        if not name:
            self.name=input("What is the name of this station?").strip().lower()
        self.leader=leader 
        #if not leader:
            #self.leader=input("What is the name of the leader of this station?")
        #copies list to items attribute
        self.items=items[:]
        #creates a new list of Item objects if none is given
        if not items:
            #creates empty list
            self.items=[]
            count=0
            count=input("How many items are there?")
            #makes sure the count variable is a digit(number) and keeps looping until a digit is entered
            while not count.isdigit():
                count=input("How many items are there?")
            #converts the number of items to an integer
            count= int(count)
            #loops through while the number of items is positive
            while count>0:
                #gets the name and the price of the new item
                name_of_item=input("What is the item's name?").strip().lower()
                item_price=input("What is the item's price?")
                #makes sure the price is a number
                while not item_price.isdigit():
                    item_price=input("What price is it?")
                #creates an item object
                item=Item(title=name_of_item, price=item_price)
                #sets that object to the proper index in the list
                self.items.append(item)
                #subtracts one from the count per loop
                count-=1
                
    def change_items(self,items):
        '''
        changes the items in the list
        takes a new list, and replaces the old one with the current one
        '''
        self.items=items[:]
        
    def add_items(self):
        '''
        adds an item to the list
        '''
        #gets a new name and price value, formats them properly
        item_name=input("What would you like to add?").strip().lower()
        item_price=input("What price is it?")
        #makes sure the price is a digit
        while not item_price.isdigit():
            item_price=input("What price is it?")
        #creates a new item object using created values
        new_item=Item(title=item_name,price=item_price)
        #adds the new item to the list of items
        self.items.append(new_item)
        
    def remove_item(self):
        '''
        removes an item from the list, taking the item to be removed
        '''        
        #gets the value of the new name and price attribute from the user, formats them properly     
        item_name=input("What is the name of the object you would like to remove?").strip().lower()
        item_price=input("What was the price of the object?")
        while not item_price.isdigit():
            item_price=input("What price is it?")
         
        #creates a new Item object       
        new_item=Item(title=item_name,price=item_price)
        
        #checks if the requested item is in the list of items, and removes it if it is present
        
        if new_item in self.items:
            #compares given Item object to every Item object in the list, and removes it if it is found
            self.items.remove(new_item)
        else:
                print("Sorry, that item isn't included")           
    
    def change_leader(self,leader2):
        '''
        changes the leader of the event, taking the name of the new leader
        '''
        self.leader=leader2 
        #if no new leader has been input already, asks for the new one
        if not leader2:
            self.leader=input("What is the name of the new leader?")
            
    def total_cost(self):
        '''
        calculates the total cost of the current event, and returns this cost
        '''
        grand_total=0
        #goes through each item in the event
        for item in self.items:
        #adds the price attribute of every item in the event to the grand total
            grand_total+=float(item.price)
         
        #returns above value   
        return grand_total
        
    
    def __str__(self):
        '''
        replaces the print statement, prints all the items from the event
        '''
        #creates a string
        text=""
        #goes through every item available, and adds the return value from the print statement for each item to a string
        for item in self.items:
            #includes a newline to separate each item
            text+="\n {}".format(item.__str__())
        #returns the created string when this object is printed
        return text
        