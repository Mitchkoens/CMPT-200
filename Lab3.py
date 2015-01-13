###################################
#Name:     Mitchell Koens
#Program:  CMPT200.Lab3.Q1
#Section:  CMPT 40L
###################################
#The main function gathers the file name from the user and then puts it into multiple other functions to gather the size, the start point, the end point, and the maze.
def main():
    filename = input ('Input the name of the maze you want to solve: ')#Gathers the name of the file the user wants to solve
    mazefile = openfile(filename)#Sends the file name into the open file function to check if the file exists and open it if it does
    if mazefile == None:#if mazefile equals none
        print("That file does not exist")#tell the user that the file does not exist
    else:
        maze = read(mazefile)#sends the open file to the read mazefile to turn it into a string
        size = getsize(maze)#sends the string holding the maze into a function to gather the line holding the size of the maze
        sizex = size[0]#gathers the x value of the size
        sizex = int(sizex)#turns size x into an integer 
        sizex = sizex * 2#multiplies size x by 2 to get the real size of the maze
        sizey = size[1]#gathers the y value of the size
        sizey = int(sizey)#turns size y into an integer
        sizey = sizey * 2#multiplies size x by 2 to get the real size of the maze
        start = getstart(maze)#sends the string holding the maze into a function to gather the line holding the start point of the maze
        startx = start[0]#gathers the x value of the start
        startx = int(startx)#turns startx into an integer
        startx = sizex - startx#minus start x from sizex to get the real startx value
        starty = start[1]#gathers the y value of the start
        starty = int(starty)#turns start y into an integer
        end = getend(maze)#sends the string holding the maze into a function to gather the line holding the end point of the maze
        endx = end[0]#gathers the x value of the end
        endx = int(endx)#turns endx into an integer
        endx = endx * 2#multiplies the end x value by two
        endx = endx - startx#subtracts start x from end x to get the real value of end x
        endy = end[1]#gathers the y value of the end
        endy = int(endy)#turns endy into an integer
        endy = endy * 2#multiply the endy value by two
        endy = endy - 1#subtracts the endy value by one to get the real endy value
        maze = removemaze(maze)#sends the string to remove maze to delete the first three strings from the list
        maze = join(maze)#Joins the lists back into one string
        maze = splitmaze(maze)#Splits the maze into a list of lists
        finished = search(maze, startx, starty, endx, endy)#Sends to the search function to find the solution
        if finished == None:#Check if there is no solution
            print('No Solution')#tell the user there was no solution
        else:#if there is a solution sends it to printt
            finished = printt(finished)#Puts the list of lists back into a string
            finished = remove(finished)#Remove the 'o's from the string and replace with ' ' to show the end string
            print(finished)#Print the final maze
            
#This function reads the maze file and gathers the start function
def openfile(filename):
    if filename == '':#If filename is blank
        filename = ('maze.txt')#change filename to maze.txt
        mazefile = open(filename)#open mazefile
        return mazefile#and return the file into the main function
    else:
        try:
            mazefile = open(filename)#open mazefile
            return mazefile#and return the file into the main function
        except IOError:#except if there is no file
            return None#return None
        
#Read the maze file and turn it into a list of strings  
def read(mazefile):
    lines = mazefile.readlines()#turns the string into one list of strings seperating by the newlines
    mazefile.close()#close the maze file 
    return lines#return the list of strings
    
#function gathers the line with the size on it
def getsize(lines):
    line = lines[0]#gathers the first row form the file
    line = line.split()#splits it to get the two values
    return line#returns the two split values to the main function

#function gathers the line with the start point on it
def getstart(lines):
    line = lines[1]#gathers the second row form the file
    line = line.split()#splits it to get the two values
    return line#returns the two split values to the main function

#function gathers the line with the end value on it
def getend(lines):
    line = lines[2]#gathers the third row form the file
    line = line.split()#splits it to get the two values
    return line#returns the two split values to the main function

#this function removes the first three rows form the list to return only the maze
def removemaze(lines):
    del lines[0:3]#Deletes the first three rows form the list
    return lines#returns the maze to the main function

#Joins the maze back into a single string from a list
def join(maze):
    line = ''.join(maze)#joins the list into a single string
    return line#returns the string that is the  maze to the main function

#Removes the 'o' from the maze and replaces it with ' '
def remove(maze):
    out = maze.replace('o', ' ')#Remove 'o' and replace with ' '
    return out#return the final maze to the function

#This function reads entire maze file and prints all the lines
def splitmaze(mazefile):
    maze = [list(row) for row in mazefile.splitlines()] #gathers all the lines of the maze 
    return maze#returns the list of lists into the main function

#This function prints the maze into something the user can see
def printt(maze):
    final = '\n'.join(''.join(row) for row in maze) # prints the maze and joins it together.
    return final#returns the string version of the solved maze into the main function

#Searches through the maze and uses recursion and backtracking to find the best solutuion to solve the maze
def search(mazeList, x, y, ex, ey):
    ex = ex#The end x value to compare to
    ey = ey#The end y value to compare to
    mazeList[ex][ey] = "E"#Turns the end value from a blank into an E
    if mazeList[x][y] == 'E':#Checks to see if the current place is the end
            mazeList[x][y] = '*'#If it is the end replacethe E with a *
            return mazeList#Returns the mazelist back to the main function
    # returns False if it encounters a wall
    elif mazeList[x][y] == '-':
        return False
    elif mazeList[x][y] == '+':
        return False
    elif mazeList[x][y] == "|":
        return False
    # returns False if it finds a visited path
    elif mazeList[x][y] == 'o':
        return False
    # marks path with '*'
    mazeList[x][y] = 'o'
    # recursive search        
    if ((search(mazeList, x+1, y, ex, ey))
            or (search(mazeList, x, y+1, ex, ey))
            or (search(mazeList, x-1, y, ex, ey))
            or (search(mazeList, x, y-1, ex, ey))):
            mazeList[x][y] = '*'
            return mazeList