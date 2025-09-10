class telefonbok:
    def __init__(self):
        self.namnlista=[]
    def create(self,name):
        for i in range(len(self.namnlista)):
            if name==self.namnlista[i][0]:
                print("That name is already in the phonebook")
                return
        self.namnlista=self.namnlista+[[name]]#lägger till ett namn med 0 nummer
    def add(self,name,number):
        for i in range(len(self.namnlista)):
            if name==self.namnlista[i][0]:#found the person        
                for j in range (1,len(self.namnlista[i])):
                    if number==self.namnlista[i][j]: #checks the numbers of person i
                        print("that number already exists.")
                        return
                self.namnlista[i]=self.namnlista[i]+[number]#found the person and the number didnt already exist
                return 
        print("that name is not in the phonebook")
        return
    def lookup(self,name):
        for i in range(len(self.namnlista)):
            if name==self.namnlista[i][0]:#found the person
                print("The person " + str(name) + " has numbers: ")        
                for j in range (1,len(self.namnlista[i])):
                    print(self.namnlista[i][j])
                
                return 
        print("that name is not in the phonebook")
        return
    def deletePerson(self,name):
        for i in range(len(self.namnlista)):
            if name==self.namnlista[i][0]:#found the person
                self.namnlista=self.namnlista[0:i]+self.namnlista[i+1:len(self.namnlista)]
                print("name " + str(name) + " was deleted from the phonebook along with its numbers")
                return 
        print("that name is not in the phonebook")
        return
    def deleteNumber(self,name,number):
        for i in range(len(self.namnlista)):
            if name==self.namnlista[i][0]:#found the person        
                for j in range (1,len(self.namnlista[i])):
                    if number==self.namnlista[i][j]: #checks the numbers of person i
                        self.namnlista[i]=self.namnlista[i][0:j]+self.namnlista[i][j+1:len(self.namnlista[i])]
                        return
                #if it goes here the number didnt exist, but no error msg is needed.
                return 
        print("that name is not in the phonebook")
        return
    def save(self,filename):
        # print(len(self.namnlista))
        # print(self.namnlista)
        with open(filename, "w") as f:
            for i in range(len(self.namnlista)):
                for j in range (0,len(self.namnlista[i])):
                      f.write(self.namnlista[i][j]+";") #since a name and its numbers are stored in a list with the name first then the numbers, this just prints all of those lists on a row.
                if (i<len(self.namnlista)-1): #the last row doesnt need to add a blank row.
                    f.write("\n")
        f.close()
    def clear(self):
        self.namnlista=[]
    def load(self,filename):
        self.clear()
        with open(filename) as f:#opens a file for reading
            while(True):
                
                x=f.readline()#reads a line from the file
                if(x==""):#read all the lines, breaks the while true loop
                    break
                clean_x=x.strip()#removes whitespace
                y=clean_x.split(";")#splits at semicolons and returns a list, that has an empty element at the end
                y=y[0:len(y)-1]

                
                #print(y)
                self.create(y[0]) #creates a person
                # print(y)
                for i in range(1,len(y)):
                    self.add(y[0],y[i]) #adds all the numbers of that person
                
        f.close()
        return

# print("hej")
def main():
    pb=telefonbok()
    while(True):
        showMenu()
        x=input("Pick an option: ")
        command=x.split(" ")
        #print(command)
        if command[0]=="create":
            pb.create(command[1])
        elif command[0]=="add":
            pb.add(command[1],command[2])
        elif command[0]=="lookup":
            pb.lookup(command[1])
        elif command[0]=="delete" and len(command)==3:
            pb.deleteNumber(command[1],command[2])
        elif command[0]=="delete" and len(command)==2:
            pb.deletePerson(command[1])
        elif command[0]=="save":
            pb.save(command[1])
        elif command[0]=="load":
            pb.load(command[1])
        elif command[0]=="quit":
            return
        
def showMenu():
    print("--------------------------------")
    print("Please pick an option: ")
    print("create name")
    print("add name number")
    print("lookup name")
    print("delete name number")
    print("delete name")
    print("save filename")
    print("load filename")
    print("quit")
    print("--------------------------------")




# pb=telefonbok()
# pb.create("nummer")
# pb.create("nummer2")
# pb.add("nummer","asd")
# pb.add("nummer", "asd2")
# pb.create("nummer3")
# pb.lookup("nummer")
# pb.deleteNumber("nummer","asd")
# pb.lookup("nummer")
# # pb.save("fil1")
# pb.load("fil1")
# print(pb.namnlista)

main()