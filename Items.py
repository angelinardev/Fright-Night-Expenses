'''
Created on Oct 9, 2018

@author: Angelina
'''
class Item(object):
    '''
    Item object
    has a title and price property
    '''
    #initializes class attributes
    def __init__(self,title,price):
        '''
        sets all the values, and asks the user to input the values if none are entered
        '''
        self.title=title.strip().lower()
        #forces input if the attribute isn't initialized when creating the object
        if not title:
            self.title=input("What is the name of the item?").strip().lower()
        self.price=price
        #forces input if the attribute isn't initialized when creating the object
        if not price:
            self.price=input("What is the price of the item?")
        #loops through while the variable isn't a digit (a number)    
        while not self.price.isdigit():
            self.price=input("What price is it?")
        
    def change_name(self):
        '''
        changes the name of the item. Takes the new name wanted
        '''
        #takes user input for a new name, formats it, sets it as the new title attribute
        self.title=input("Enter the new name of the item").strip().lower()
            
    def change_price(self):
        '''
        changes the price of the item. Takes the new price wanted.
        '''
        #takes user input for a new price
        self.price=input("Enter the new price")
        #loops while the price is not a digit (number)
        while not self.price.isdigit():
            self.price=input("What price is it?")
    
    def __str__(self):
        '''
        replaces the print function for the Item object
        '''
        #gets the name and price of the item
        name_of_item=self.title
        price_of_item=self.price
        #creates a string that nicely formats the name and price together
        text="Name:{} \t Price: ${} \n".format(name_of_item,price_of_item)
        #the output that appears when printing
        return text
    
    def __eq__(self,other):
        #when comparing objects of this type, compares the title value and price value to those of the other Item object
        return self.title == other.title and self.price==other.price
        