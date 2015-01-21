########################################
#Name:     Mitchell Koens
#Program:  CMPT200.Lab.6.Class
########################################
class Node:
    def __init__(self, data = 0, count = 1):
        self.left = None #left leaf
        self.right = None #Right leaf
        self.data = data #Data of the node
        self.count = count #Count of the data
        
    # add data to the tree in a sorted manner
    def insert(self, data):
        # add one to the frequency count if the data equals the node already in the tree
        if data == self.data:
            self.count += 1
        # if data is less than the current node go left
        elif data < self.data:
            # if no data here, make a new node
            if self.left == None:
                self.left = Node(data)
            # else try the same on its left child
            else:
                self.left.insert(data)
        # if its greater, go right
        else:
            # if no data here, make a new node
            if self.right == None:
                self.right = Node(data)
                 
            # else try the same on its right child
            else:
                self.right.insert(data) 

        #Gather amount of unique words
    def length(self):
        # if no children, return this nodes data as a list
        if self.left == None and self.right == None:
            return [self.data]
        # create empty list
        li = []
        # append the first list
        if self.left is not None:
            li.extend(self.left.length())
        # append data
        li.append(self.data)
        # append the second list
        if self.right is not None:
            li.extend(self.right.length())
        return li
    
    # Used to print out the unique words and their frequency
    def frequency(self):
        # if no children, return this nodes data as a list
        if self.left == None and self.right == None:
            return [("Word: " + self.data + " frequency: " + str(self.count))]
        # create empty list
        li = [] 
        # append the first list
        if self.left is not None:
            li.extend(self.left.frequency())
        # append data
        li.append(("Word: " + self.data + " frequency: "  + str(self.count)))
        # append the second list
        if self.right is not None:
            li.extend(self.right.frequency())  
        return li #return the list

    def searchfrequency(self):
        if self.left == None and self.right == None:
            return [(self.data, str(self.count))] #If the node terminates return the data and its count
        #Create an empty list
        li = [] 
        if self.left is not None: 
            li.extend(self.left.searchfrequency())#puts all the left leafes into the list
        li.append((self.data, str(self.count)))#Append the new data into the list
        if self.right is not None:
            li.extend(self.right.searchfrequency())#Puts all the right leafs into the list  
        return li #Return the list