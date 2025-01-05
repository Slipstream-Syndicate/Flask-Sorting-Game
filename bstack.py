# Assignment 3 - B-Stack
'''
Name > Abdul Basit
Student ID > 1808633
Date > March 11 - 18, 2023
'''

class Stack:
    '''
    This function creates the stack for the flasks.
    '''
    def __init__(self, size):
        self.items = []
        self.size = size
    
    def Pour_In(self, item):
        
        if len(self.items) < self.size:
            self.items.append(item)
    
    def Get_Items(self):
        return self.items
    
    def Pour_Out(self):
        if self.items != []:
            return self.items.pop()
        raise Exception("Flask is Empty")
    
    def peek(self):
        if self.items != []:
            return self.items[len(self.items)-1]
        raise Exception("Flask is Empty")
        
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def show(self):
        print(self.items)
        
    def seal(self):
        
        if len(set(self.items)) == 1 and len(self.items) == 3:
            return True
        return False

    def isFull(self):
        if len(self.items) == 4:
            return True
        return False
    
    def __str__(self):
            
        pass
    
    def clear(self):
        #TO DO: complete method according to updated ADT
        if self.items != []:
            self.items.clear()
