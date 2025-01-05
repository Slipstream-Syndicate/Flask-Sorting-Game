# Assignment 3 - B-Queue
'''
Name > Abdul Basit
Student ID > 1808633
Date > March 11 - 18, 2023
'''

import sys
import os
import time
from bqueue import BoundedQueue
from bstack import Stack

Max_Capacity = 4
os.system("")  # enables ANSI characters in terminal

ANSI = {
    'RED':'\033[31m', 
    'GREEN':'\033[32m',
    'AA': '\033[31m\033[41m', # Red
    'BB': '\033[34m\033[44m', # Blue
    'CC': '\033[32m\033[42m', # Green
    'DD': '\033[38;5;208m\033[48;5;208m', # Orange
    'EE': '\x1b[33m\x1b[43m', # Yellow
    'FF': '\x1b[35m\x1b[45m', # Purple
    'GG': '\033[47m', # White
    'RESET': '\033[0m',
    'CLEARLINE': '\033[K'
}

                
def clear_screen():
    '''
    Clears the terminal screen for future contents.
    Input: N/A
    Returns: N/A
    '''
    if os.name == "nt":  # windows
        os.system("cls")
    else:
        os.system("clear")  # unix (mac, linux, etc.)

def display_error(error):
    '''
    Displays an error message under the current site as specificed by "error".
    Input:
    - error (str): error message to display
    Returns: N/A
    '''
    print("\033[{1};{0}H{2}".format(0, 5, error))

    
def print_header():
    '''
    Prints the BROWSE-175 header.
    Input: N/A
    Returns: N/A 
    '''
    print("\033[{1};{0}H{2}".format(0, 0, "Magical Flask Game"))
    
def move_cursor(x, y):
    '''
    Moves the cursor to the specified location on the terminal.
    Input:
    - x (int): row number
    - y (int): column number
    Returns: N/A
    '''
    print("\033[{1};{0}H".format(x, y), end='')


class Flask_Game:
    '''
    This class creates the flasks after the reading the text file and adds the chemicals accordingly.
    '''
    def __init__(self, capacity):
        self.capacity = capacity
        self.Flask_Dict = {}   
            
    def Levels(self, Filename):
        '''
        This function initializes the queue for chemicals and the flasks. It then enqueues the chemicals into the the queuea and eventually pushes them into the respective flasks.
        Input : Filename
        Return : Number of Flasks
        '''         
        
        Flask_Dict = {}
        Chemicals = BoundedQueue(self.capacity)
        
        with open(Filename, 'r') as File:
            
            self.Number_of_Flasks = int(File.readline().strip().split()[0])
            
            for Index in range(self.Number_of_Flasks):
                
                self.Flask_Dict[str(Index+1)] = Stack(self.capacity)

            Key = list(self.Flask_Dict.keys())
                
            Data = File.readlines()
            
            for Item in Data:
                Item = Item.strip('\n')
                
                if len(Item) == 2:
                    
                    Chemical = ANSI[Item.strip()]+Item.strip()+ANSI["RESET"]
                    Chemicals.Pour_In(Chemical)
                
                if len(Item) == 3:
                    
                    Number_of_Chemicals = int(Item.split('F')[0])
                    Flask_Number = int(Item.split('F')[1])
                    
                    for Index in range(Number_of_Chemicals):
                        
                        Chemical = Chemicals.Pour_Out()
                        
                        if Chemical:
                        
                            self.Flask_Dict[str(Flask_Number)].Pour_In(Chemical)
            
            return self.Number_of_Flasks
            # move cursor
            # display flasks

    
    def Display_Flasks(self, source, destination):
        """
        This function displays the flasks with proper formatting based on the instructions.
        Input : Source Flask, Destination Flask
        Return : None
        """
        self.Flask_Values = list(self.Flask_Dict.values())
        
        Four_Flasks = self.Flask_Values[0:4]
        move_cursor(0,6)
        
        for Index in range(self.capacity-1, -1, -1):
            
            for Item in Four_Flasks:
                
                Items = Item.Get_Items()
                if Item.seal():
                    
                    if Index == self.capacity-1:
                        print("+--+", end="  ")
                        
                    elif Index < self.capacity-1:
                        print(f"|{Items[Index]:^2}|", end = "  ")
                
                else:
                    
                    if Index < len(Items):
                        print(f"|{Items[Index]:^2}|", end = "  ")
                    else:
                        print("|  |", end = "  ")
            print()
        
        for Index in range(len(Four_Flasks)-1, -1, -1):
            print("+--+", end="  ")
        print()
        
        move_cursor(0,11)

        
        for Index in range(len(Four_Flasks)):
            
            if (source != None) and (int(source) == (Index+1)):
                
                print(ANSI["RED"]+f"  {Index+1}"+ANSI["RESET"], end = "   ")
            
            if (destination != None) and (int(destination) == (Index+1)):

                print(ANSI["GREEN"]+f"  {Index+1}"+ANSI["RESET"], end = "   ")
            
            elif (source != None) and (destination != None) and (int(source) != (Index+1)) and (int(destination) != (Index+1)):
                
                print(f"  {Index+1}", end = "   ")  
            
            elif (source == None) and (destination == None):
                
                print(f"  {Index+1}", end = "   ")    
                    
        if self.Number_of_Flasks == 8:                    
            
            move_cursor(0, 13)
            
            Last_Four = self.Flask_Values[4:]
            
            for Index in range(len(Last_Four)-1, -1, -1):
                
                for Item in Last_Four:
                    
                    Items = Item.Get_Items()
                    if Item.seal():
                        
                        if Index == self.capacity-1:
                            print("+--+", end="  ")
                            
                        elif Index < self.capacity-1:
                            print(f"|{Items[Index]:^2}|", end = "  ")
                    
                    else:
                        
                        if Index < len(Items):
                            print(f"|{Items[Index]:^2}|", end = "  ")
                        else:
                            print("|  |", end = "  ")
                print()
            
            for Index in range(len(Last_Four)-1, -1, -1):
                print("+--+", end="  ")
            print()
            
            move_cursor(0,18)
    
            
            for Index in range(len(Last_Four)):
                
                if (source != None) and (int(source) == (Index+5)):
                    
                    print(ANSI["RED"]+f"  {Index+5}"+ANSI["RESET"], end = "   ")
                
                if (destination != None) and (int(destination) == (Index+5)):
    
                    print(ANSI["GREEN"]+f"  {Index+5}"+ANSI["RESET"], end = "   ")
                
                elif (source != None) and (destination != None) and (int(source) != (Index+5)) and (int(destination) != (Index+5)):
                    
                    print(f"  {Index+5}", end = "   ")  
                
                elif (source == None) and (destination == None):
                    
                    print(f"  {Index+5}", end = "   ")            
            
            
    def Check_Input_Source(self, source):
        """
        This function check whether the input is correct or invalid.
        """
        self.source = source
        
        try:
            self.source = int(self.source)
            return True
            
        except:
            if self.source.lower() == "exit":
                return True
            else:
                raise Exception("Invalid Input. Try again.")
    
    def Check_Input_Destination(self, destination):
        """
        This function check whether the input is correct or invalid.
        """
        self.destination = destination 
        
        try:
            self.destination = int(self.destination)
            return True
            
        except:
            if self.destination.lower() == "exit":
                return True
            else:
                raise Exception("Invalid Input. Try again.")  
        
    def perform_operation(self, source, destination):
        """
        This function handles the movement of chemicals between the flasks.
        Input : Source Flask, Destination Flask
        Return : None or Exception
        """            
            
        if int(source) < 0 or int(source) > self.Number_of_Flasks:
            raise Exception("Invalid Input. Try again.")
        
        if int(destination) < 0 or int(destination) > self.Number_of_Flasks:
            raise Exception("Invalid Input. Try again.")          
        
        if int(source) == int(destination):
            move_cursor(0,5)
            raise Exception("Cannot pour into same flask. Try again.")
        
        if self.Flask_Dict[str(source)].seal():
            raise Exception("Cannot pour from that flask. Try again.")
        
        if self.Flask_Dict[str(destination)].seal():
            raise Exception("Cannot pour into that flask. Try again.")     
        
        if self.Flask_Dict[str(destination)].isFull():
            raise Exception("Cannot pour into that flask. Try again.")     
            
            
        self.chemical = self.Flask_Dict[str(self.source)].Pour_Out()
        self.Flask_Dict[str(self.destination)].Pour_In(self.chemical)
        
    def check_win(self):
        """
        This function checks whether the player has won the game.
        Input : None
        Return : True if Game is WON else False
        """
        self.Complete_Flasks = 0

        for Index in range(self.Number_of_Flasks):
                
            if self.Flask_Dict[str(Index+1)].seal() or self.Flask_Dict[str(Index+1)].isEmpty() == True:
                
                self.Complete_Flasks += 1
                
        if self.Complete_Flasks == self.Number_of_Flasks:
            
            return True
        
        return False
        
    def print_win_msg(self):
        """
        This function prints the WIN message after the game is WON.
        Input : None
        Return : None
        """
        if self.Number_of_Flasks == 4:
            move_cursor(0, 13)
            print("Level Complete!")
            
        elif self.Number_of_Flasks == 8:
            move_cursor(0,20)
            print("Level Complete!")
        
def main():
    """
    This function handles the execution of the game.
    """
    Levels = ["level1.txt", "level2.txt", "level3.txt", "level4.txt", "level5.txt", "level6.txt", "level7.txt"]
    Level_Index = 0
    for level in Levels:
        Level_Index += 1
        if Level_Index == 7:
            for Index in range(3):
                clear_screen()
                print("BOSS LEVEL")
                time.sleep(1)
        Error = None
        Game = Flask_Game(Max_Capacity)
        Game.Levels(level)
        gameOver = False
        clear_screen()
        print_header()
        Game.Display_Flasks(None, None)
        Index = 0
        while not gameOver:
            
            if Index != 0:
                clear_screen()
                print_header()
            
            try:
                
                if Error != None:
                    print(Error)
                move_cursor(0,3)
                print('Select source flask:')
                move_cursor(0,4)
                print("Select destination flask:")
                move_cursor(len('Select source flask:')+1, 3)
                Source_Flask = input()
                Check_Source = Game.Check_Input_Source(Source_Flask)
                if Check_Source != True:
                    continue
                if Source_Flask.lower() != 'exit':
                    move_cursor(len("Select destination flask:")+1, 4)
                    Destination_Flask = input()
                    Check_Destination = Game.Check_Input_Destination(Destination_Flask)
                    if Check_Destination != True:
                        continue
                    if Destination_Flask.lower() != 'exit':
                        move_cursor(0,5)
                        print(ANSI["CLEARLINE"])
                        Game.perform_operation(Source_Flask, Destination_Flask)
                        Game.Display_Flasks(Source_Flask, Destination_Flask)
                    else:
                        clear_screen()
                        print("Game Over")
                        clear_screen()
                        move_cursor(0,0)
                        sys.exit()                  
                    
                else:
                    clear_screen()
                    print("Game Over")
                    clear_screen()
                    move_cursor(0,0)
                    sys.exit()
                
            except Exception as e:
                Error = display_error(e.args[0])
            
            move_cursor(len('Select source flask:')+1, 3)
            print(ANSI["CLEARLINE"])
            move_cursor(len("Select destination flask:")+1, 4)
            print(ANSI["CLEARLINE"])     
            
            if Game.check_win():
                clear_screen()
                print_header()            
                move_cursor(0,3)
                print('Select source flask:')
                move_cursor(0,4)
                print("Select destination flask:")  
                move_cursor(0,5)
                print(ANSI["CLEARLINE"])
                Game.Display_Flasks(Source_Flask, Destination_Flask)
                Game.print_win_msg()
                time.sleep(1)
                gameOver = True

        if Level_Index != 7 and Game.check_win():
            Run = True
            while Run == True:
                clear_screen()
                move_cursor(0,0)
                Continue_Input = input("Do you want to proceed to the next level? [Y/N]\n>")
            
                if Continue_Input.upper() == 'Y':
                    Run = False
                elif Continue_Input.upper() == 'N':
                    sys.exit()
                else:
                    print("Invalid Input")
                    time.sleep(0.6)
        
        if Level_Index == 7 and Game.check_win():
            clear_screen()
            print("CONGRATULATIONS YOU HAVE COMPLETED ALL LEVELS!")
            time.sleep(1)

if __name__ == "__main__":
    main()
