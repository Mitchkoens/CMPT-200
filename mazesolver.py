########################################
#Name:     Mitchell Koens
#Program:  CMPT200.Lab.3
########################################
#This is the main function taking together all of the other functions to read the maze
def main():
    location = [] #location to store areas visited
    hasNoEnd = True #if the area has no solution tell the user
    FileName = input("Input the name of the maze file you want to solve: ")#ask the user which file they wish to input if a "" enptry string go to the defalut maze.txt
    if FileName == "":
	mazefile = ('maze.txt')
	mazefile = open(FileName, "r")
    else:
	try:#for error checking
	    mazefile = open(FileName, "r")#opens the file in a read only format
	except IOError:#Error checking for if the file does not exist askes user again for another file
	    print('that file does not exist')
	    FileName = input('Try another file last try: ')#get the users input a file name again
	    try:#for error checking
		mazefile = open(FileName, "r")#opens the file in a read only format
	    except IOError:#IOerror making sure the program does not crash if the user enters a file that does not exist
		print('File does not exist using preset file')#Tell the user that the file doesnt exist and program will end
		mazefile = ('maze.txt')
		maze = splitmaze(mazefile) # use the splitmaze function to get the maze
		S = splitstart(mazefile) #use the splitstart function to get the start point
		E = splitend(mazefile) # use the splitend function to get the end point
		for y in range(0, len(mazefile)):
		    for x in range(0, len(maze[y])):
			if maze[y][x] == S:
			    location = [y, x]
			elif maze[y][x] == E:
			    hasNoEnd = False
			    if len(location) == 0:
				raise Exception("No start cell found, check your input file")   #if no start cell is found tell the user
			    if hasNoEnd:
				raise Exception("Maze has no end, unsolvable.") # if the maze has no end tell the user it is unsolvable
			    recursive(maze, location[0], location[0]) #call the recursive function

#This function reads the maze file and gathers the start function
def splitstart(mazefile):
    infile = open(mazefile, 'r') #gets the file
    start = [list(row) for row in infile.read().split("\n")] #splits the file where the new lines are
    start = start[1] #chose the spot to grab the start values from
    infile.close()# close the file when done
    return start

#This function reads the maze file and gathers the End function
def splitend(mazefile):
    infile = open(mazefile, 'r') #gets the file
    end = [list(row) for row in infile.read().split("\n")] #splits the file where the new lines are
    end = end[2] #chose the spot to grab the end values from
    infile.close() # close the file when done
    return end

#This function reads entire maze file and prints all the lines
def splitmaze(mazefile):
    infile = open(mazefile, 'r') #gets the file
    maze = [list(row) for row in infile.read().splitlines()] #gathers all the lines of the maze 
    infile.close() # close the file when done
    return maze
#This function prints the maze into something the user can see
def printt(maze):
    print('\n'.join(''.join(row) for row in maze)) # prints the maze and joins it together.
    
#The recursive function which searches through the maze to find the end
def recursive(maze, y, x):
    printt(maze)
    if maze[y][x] in (' ', S):
	maze[y][x] = '*'#fill in the blanks with a star where the path goes
        if (recursive(maze, y, x+1) or recursive(maze, y-1, x) or  #decide which way to move
            recursive(maze, y, x-1) or recursive(maze, y+1, x)):
            maze[y][x] = ' '
            return True
    elif maze[y][x] == E:
        return True 
    return False
#Initalizes the maze
if __name__ == "__main__":
    main()
