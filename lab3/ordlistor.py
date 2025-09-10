


def ordlistaListor():
    keys=[]
    values=[]
    while(True):
        printmenu()
        x=takeInputMenu()
        if(x=="1"):

            (keys,values)=addWordForLists(keys,values)  
        if (x=="2"):
            lookupInLists(keys,values) #function to find the corresponding value to a key/word someone looks for.
        if (x=="3"): #exits the program
            return
def addWordForLists(keys,values):
    newKey=input("Word to insert: ")
    if (newKey in keys):
        print("That word is already in the dictionary")
        return (keys,values) #no new key added
    else:
        newValue=input("Description of word: ")
        return (keys+[newKey],values+[newValue]) #new key added
def printmenu(): #prints basic menu
    print("Menu for dictionary")
    print("1: Insert")
    print("2: Lookup")
    print("3: Exit program")
def takeInputMenu():#takes input for menu options
    x=input()
    if(x!="1" and x!="2" and x!="3"):
        print("invalid input")
        return(takeInputMenu())
    return x
def lookupInLists(keys,values): #finds a value or prints that it doesnt exist
    find=input()
    for i in range(len(keys)):
        if keys[i]==find:
            print("Description of the word " + keys[i] + " is: " +values[i])
            return
    
    print("that word is not in the dictionary")




def ordlistaTupler():
    tupelList=[]
    while(True):
        printmenu()
        x=takeInputMenu()
        if(x=="1"):
            tupelList=addWordForTupels(tupelList)  
        if (x=="2"):
            lookupInTupleList(tupelList) #function to find the corresponding value to a key/word someone looks for.
        if (x=="3"): #exits the program
            return
def addWordForTupels(tupelList):
    newKey=input("Word to insert: ")
    for i in range(len(tupelList)):
        if tupelList[i][0]==newKey:
            print("That word has already been added")
            return
    newValue=input("Description of word: ") #if it wasnt added we ask for the description here.
    return tupelList+[(newKey,newValue)]

def lookupInTupleList(tupelList):
    key=input("What word do you want to lookup: ")
    for i in range(len(tupelList)):
        if tupelList[i][0]==key:
            print("Description for " + key + " is: " + tupelList[i][1]) #find the right word, if its not here it doesnt exist.
            return
    print("That word is not in the dictionary.")




def ordlistaDictionary():
    dictionary={}
    while(True):
        printmenu()
        x=takeInputMenu()
        if(x=="1"):
            dictionary=addWordForDict(dictionary)  
        if (x=="2"):
            lookupInDict(dictionary) #function to find the corresponding value to a key/word someone looks for.
        if (x=="3"): #exits the program
            return
        
def addWordForDict(dict):
    newKey=input("Word to insert: ")
    if (dict.get(newKey)):
        print("That word is already in the dictionary") #checks if the word exists already in the dictionary
        return dict
    
    newValue=input("Description of word: ") #if it wasnt added we ask for the description here.
    dict[newKey]=newValue
    return dict

def lookupInDict(dict):
    key=input("What word do you want to lookup: ")
    
    if dict.get(key):
        print("Description of word: "+ dict.get(key)) #find the right word, if its not here it doesnt exist.
        return
    print("That word is not in the dictionary.")
ordlistaListor()
ordlistaTupler()
ordlistaDictionary()
