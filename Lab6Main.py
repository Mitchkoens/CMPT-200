########################################
#Name:     Mitchell Koens
#Program:  CMPT200.Lab.6.Main
########################################
from Lab6Class import *
# Binary Tree Sort
def BinaryTreeSort(li):
    # create the root node with the first element
    root = Node(li[0])
    # add each element to the tree
    for i in range(1, len(li)):
        root.insert(li[i])   
    #gather the frequency
    return root.frequency()

def BinaryTreelength(li):
    # create the root node with the first element
    root = Node(li[0])
    # add each element to the tree
    for i in range(1, len(li)):
        root.insert(li[i])
        #Gather the length
    return root.length()

def Search(find, li):
    # create the root node with the first element
    root = Node(li[0])
    # add each element to the tree
    for i in range(1, len(li)):
        root.insert(li[i])
    lis = root.searchfrequency()
    n = 0 # Start n at zero to start the search through the file
    while n != (len(lis)): # as long as n does not equal the length of the list
        if lis[n][0] == find: #If the character in the first spot of the nth search through matches the character
            return lis[n][1] # Return the amount of occurences the found word has
        else: #else if list does not == find increase n by 1
            n += 1 #Increase n by 1
    return False #If find is not found in the document return false

def manipulate():
    file = input("Which document do you want to use? ")
    if file == '':#If filename is blank
        return None
    else:
        try:
            myfile = open(file)#open file
            punctuation = [':', '"', ';', '<', '>', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '?','/',',','[',']','{','}','|', "-"] #Punctuation to be removed from the file
            read = myfile.read().replace('.', '')#Strip the punctuation from the txt document
            for i in punctuation: #Goes through the punctuation to be removed
                read = read.replace(i, '') #Start the stripping of the punctuation
            read = read.lower()#put the document into lowercase format
            read = read.split()#split the document into a list   
            return read        #return the list of the documents txt
        except IOError:#except if there is no file
            return None#return None    

def main():
    read = manipulate()#Gathers the string made from the file 
    if read == None: #If there is no string exit the program
        print("That file does not exist exiting program") #Tell the user the file does not exist exit the program
        return #Exit the program
    true = True #Make true Equal true
    while true: #As long as true is still true
        inp = input("Do you want to\n1) Find out how many unique words there are?\n2) A print out of the words and the frequency in which they occur?\n3) Search for a specific word and its frequency and the precentage of the  document it makes up?\nEnter any other number to exit the menu: ") #gathers the user input
        while inp.isdecimal() == False: # while input is not a decimal continue to show the menu
            print("That is not one of the menu choices bring back to the menu\n") #Tell the user they are going back to the menu
            inp = input("Do you want to\n1) Find out how many unique words there are?\n2) A print out of the words and the frequency in which they occur?\n3) Search for a specific word and its frequency and the precentage of the  document it makes up?\nEnter any other number to exit the menu: ")   #gathers the user input
        inp = int(inp) # turn input into an interger
        if inp == 1: #Check if the users input equals 1 
            length = BinaryTreelength(read) #this section gathers length of the unique words list
            length = len(length) #and prints out the lenght of the list
            print ("The amount of unique words are: "+ str(length))
        elif inp == 2: #Checks if the users input equals 2 
            frequency = BinaryTreeSort(read) #This section prints out the list of the unique words and the frequency of the words
            for elem in frequency: #This allows for printing the list on multiple lines
                print (elem) #Print current elem at in the list
        elif inp == 3: #Checks if the users input equals 3
            length = BinaryTreelength(read) #Gather the length
            length = len(length)#Gathers the length
            find = input("Which word do you want to search for? ") #gather the word the user wants to find
            find = find.lower() #Lower case the word so that it equals the list
            search = Search(find, read) #Goes to the search function
            if search == False: #If search returned false 
                print(find + " was not in the document.") #Tell the user there word was not in the document
            else:
                percent = ((int(search) / length) * 100) #Gather the precent of the document that the word makes up
                print(find + " was in the document " + search + " times which is " + str(percent) + "% of the document") #Tells the user there word was in the document, tell them the amount of time and the recent of the document it makes up
        elif inp >= 0: #If input = or is less than zero  turn true to false to exit the menu
            true = False #Turns true to false
        elif inp <= 4: #If true is = to or greather than 4 turn true to false and exit the menu
            true = False #Turn true to false
    return #Exits the file when the while loop is exited 