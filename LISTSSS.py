#David Pina  
#01/10
#To do list

#initialize
answer = input("What do you want in your list")
List = [answer]


#functions
#Runs the actual todo program that provides a menu for options that the list does
def Todoprogram(): 
    print("1.Show list       2.Insert Task        3.Mark completed        4. Delete Task     5.Close     6.Clear List      7.Sort List Alphabetically    8.Amount of Items")
    answer2 = int(input("Please choose a option"))
    if answer2 ==1:
        print(List)
        Todoprogram()
    elif answer2 ==2:
        insertTask()
        Todoprogram()
    elif answer2 ==3:
        markcomplete()
        Todoprogram()
    elif answer2 ==4:
        removetask()
        Todoprogram()
    elif answer2 ==5:
        print("Goodbye")
    elif answer2 == 6:
        clearlist()
        Todoprogram()
    elif answer2 == 7:
        sortalph()
        Todoprogram()
    elif answer2 == 8:
        itemcount()




#inserts a task into the to do list
def insertTask():
    addedtask=input("what food do you want added")
    locationtask = int(input("where should it be placed?")) 
    List.insert(locationtask,addedtask)
#removes a task from the todo list
def removetask():
    removedtask = input("What food do you want removed")
    List.remove(removedtask)

#Marks the chose task as a complete with a X
def markcomplete():
    complete = input("what is completed")
    List.remove(complete)
    List.append("X" + complete)

def clearlist():
    List.clear()

def sortalph():
    sorted(List)

def itemcount():
    listcount = int(len(List))
    print("Items in list " + str(listcount))

#Main
Todoprogram()

