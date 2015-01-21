###################################
#Name:     Mitchell
#Program:  CMPT200.Lab7.Q1
#Section:  CMPT 40L
###################################
import ctypes
import random
#Main program askes the user which Sorting method they would like to use and the size of the array the user wants to sort
#shows the un sorted array and the sorted array
def main():    
    arrSize = input("How large of an array would you like to solve: ") #Ask the user the size of the array they want to sort
    while arrSize.isdecimal() == False: #While loop used to make sure user enters only numbers for the array size
        print ("Only numbers allowed")#If the user enters a value that cannot be turned into an integer
        arrSize = input("How large of an array would you like to solve: ") #Ask the user again what size of an array they would like
    arrSize = int(arrSize) #Turns the string the user entered into an integer       
    lst = List(arrSize) #Gather the shuffled list to turn into an array
    print(lst)
    printarray(arrSize, lst)
    seq = returnarray(arrSize, lst) #Turn the shuffled list into an array and print the array
    print (seq)
    true = True #make true equal to true
    while true: #As long as true is is true continue through the menu options
        choice = input('Which sorting algorithim do you want to use\n 1: QuickSort\n 2: MergeSort\n 3: SelectionSort\n 4: HeapSort\n Enter any other number to exit the program: ') #Ask the user which program they want to use to sort the array and tells them how to exit the menu
        while choice.isdecimal() == False: #A while loop used to make sure the menu choice is a decimal
            print ("Only numbers allowed")#If the user enters a value that cannot be turned into an integer
            choice = input('Which sorting algorithim do you want to use\n 1: QuickSort\n 2: MergeSort\n 3: Selection\n 4: Exit\n Enter any other number to exit the program: ') #Ask the user which program they want to use to sort the array and tells them how to exit the menu
        choice = int(choice) #Turns the string the user inputs into an integer
        if choice == 1:  #If user entered a value of 1 insert the function quickSort
            quick = quickSort(seq) #outputs the result of the quicksort method 
            print(quick)
            #printarray(arrSize, quick) #Turns the sorted list into an array and prints it
        elif choice == 2:  #If user entered a value of 2 insert the function MergeSort
            merge = mergeSort(seq) #outputs the result of the MergeSort function
            #print(merge)
            printarray(arrSize, merge) #Turns the sorted list into an array and prints it
        elif choice == 3:  #If user entered a value of 3 insert the function selectionSort
            selection, count = selectionSort(seq) #outputs the result of the SelectionSort
            counts(count) #Gathers the counts from the selection sort and prints out the amount of counts
            #print(selection)
            printarray(arrSize, selection) #Turns the sorted list into an array and prints it
        elif choice == 4:  #If user entered a value of 4 insert the function exit
            heap, count = heapsort(lst) #Gather the result of the heap sort
            counts(count) #Gathers the counts from the selection sort and prints out the amount of counts
            #print(heap)
            printarray(arrSize, heap) #Turns the sorted list into an array
        elif choice >= 0: #If the user enters 0 or a lower value turn true to false to exit the menu
            true = False #Make true equal to False
        elif choice <= 5: #If the user enters 5 or a higher value turn true to false to exit the menu
            true = False #Make true equal to false
#Shuffling the list that is made into the ctype array
def shuffle(x):
    x = list(x) #Turns x into a list
    random.shuffle(x) #Shuffles the list x
    return x #returns the shuffled list

#This function prints out the counts
def counts(count):
    print("This Program has", count, "counts")#Print out the amount of counts the program has
    
#This function makes the list that the program uses to make the array
def List(size):
    array = [] #an empty list
    for i in range(1, size + 1): #Enters the values from one to the size the user enters
        array.append(i) #Appends the value of i into the array list
    array = shuffle(array) #Shuffles the list
    return array #returns the shuffles list

#This function takes the list and makes it into an array
def printarray(size, array):
    arr = (ctypes.c_int * size)(*array) #Makes the array of the size given
    arr = (' '.join(str(i) for i in arr)) #Puts the array into a string to print it on one line
    print (arr) #Print the string of the array

def returnarray(size,array):
    arr = (ctypes.c_int * size)(*array) #Makes the array of the size given
    arr = (' '.join(str(i) for i in arr)) #Puts the array into a string to print it on one line 
    return (arr)

######QuickSort Algorithim######
#This is the function to quick sort the array
def quickSort(arr):
    count = 0 #Starts the count
    count += 1 #Adds one to the count everytime quicksort is called
    size = len(arr) #Gathers the length of the list
    less = [] #creates a blank list to put the less into
    pivotList = [] #create a blank list to put the pivot point in 
    more = [] #create a blank list
    if len(arr) <= 1: #if the length of the list is less than or equal to one
        return arr #return the arr
    else:
        pivot = arr[0] #Makes the pivot point the first value in the list
        for i in arr: 
            if i < pivot: #If i is less than the pivot point append i into the list of less
                count += 1 #Add one into count for the comparison used
                less.append(i) #Append i into the less list
            elif i > pivot: #If i is greater than the pivot point append i into the list of more
                count += 1 #Add one into the count for the comparison used
                more.append(i) #Append the i into the more list
            else:
                count += 1 #Add one to the count for the comparison used
                pivotList.append(i) #If the i is equal to the pivot point append to the pivot list
        less = quickSort(less) #Recurse through the quicksort with less as the list entered continue through until less equals one
        count += 1 #Add one for the recusion used
        more = quickSort(more)#Recurse through the quicksort with more as the list entered continue through until less equals one
        count += 1 #Adds one for the recursion used
        array = less + pivotList + more #Add the values at less, pivotList, and more into the list
        counts(count) #Call in the counts function which prints out the amount of counts the program has
        return array #return the list of the array
    
######MergeSort Algorithim######
#This is the function used to merge sort the array
def mergeSort(arr):
    count = 0 #Starts the count
    count += 1 #Adds one to the count each time the mergeSort is called
    result = [] #Creates an empty list for the result
    if len(arr) < 2: #check if the length of the array is less than two
        return sorted(arr) #if the length of the array is less than two return sorted array
    mid = int(len(arr)//2) #Get the mid point of the array by dividing the length of the array by two
    y = mergeSort(arr[:mid]) #y returns the values to the left of mid
    z = mergeSort(arr[mid:]) # x returns the values to the right of mid
    i = 0 #i equals 0
    j = 0 #j equals 0
    while i < len(y) and j < len(z):
            if y[i] > z[j]: #Check is y[i] is greater thn z[j]
                result.append(z[j]) #  y[i] is greater append into result the value of z[j]
                j += 1 #move to the next point in j
                count += 1 #Add one to the count because there is a comparison
            else: #y[i] is less than z[j]
                result.append(y[i]) #y[i] is less append into result the value of y[i]
                i += 1 #move to the next point in i
                count += 1 #Add one to the count because there is a comparison
    result += y[i:] #Add the sorted values in y into result
    result += z[j:] #Add the sorted values in z into result
    counts(count)
    return result #Returns result which is the sorted list

######SelectionSort Algorithim######
#This function is used to sort the array using selection sort
def selectionSort(arr):
    count = 0 #Start the count at zero
    count += 1 #Add one to the count
    for i in range(0,len(arr)-1):
        mn = min(range(i,len(arr)), key=arr.__getitem__)
        arr = int(arr)
        arr[i],arr[mn] = arr[mn],arr[i] #Compare between 
        count += 2 #Add two to the count every time the for loop goes through itself for the 2 comparisons the function has on the line before
    return arr, count #Returns the value of the sorted array


######HeapSort Algorithim######
#This function is used to sort the array using a heap sort algorithim
def heapsort(arr):
    for start in range((len(arr)-2)//2, -1, -1):
        siftdown(arr, start, len(arr)-1)
    for end in range(len(arr)-1, 0, -1):
        arr[end], arr[0] = arr[0], arr[end]
        siftdown(arr, 0, end - 1)
    return arr, count

def siftdown(arr, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end: break
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break
