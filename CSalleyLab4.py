#Christopher Salley
#Project 4: Cash Register
#If you reomove a product in remove mode and then try to request that item in sale made it will
#put out an error

from tkinter.filedialog import askopenfilename
filename = askopenfilename()    #Ask the user to open the certain file for Cash Register
fileObject = open(filename, "r")    #open and read the excelfile with words
filelines = (fileObject.readlines())    #Puts excelfile in individual lines
productList = {}    #Creates a dictionary for all the lines from excelfile

class Product:  #Creates a class
    def __init__(self,upc7,upc10,manufacturer,description,cost):    #Created from the class and it allows the class to initialize the attributes of a class.
        self.upc7 = upc7    #Access the attributes and methods of the class for upc7
        self.upc10 = upc10  #Access the attributes and methods of the class for upc10
        self.manufacturer = manufacturer #Access the attributes and methods of the class for manufacturer
        self.description = description  #Access the attributes and methods of the class for description
        self.cost = cost #Access the attributes and methods of the class for cost

for x in filelines:
    product = x.split(',')  #Splits one line at a time in the file makes product as a list
    tempproduct = Product(product[1],product[2],product[3],product[4],float(product[5][0:-1]))  #Makes tempproduct
    productList[int(product[0])] = tempproduct  #Puts that tempproduct into the dictionary


SaleList = {} #Creates a dictionary for the products
run = True
Letter = " "
runningTotal = 0    #This keeps track of total in sale mode
while run == True:
    userIn = input("Please enter a letter.\n")  #Will ask the user to enter a letter and if its anything other than R,r,N,n,S,s then it
                                                #will ask for the user to enter a letter again
    if userIn == "R" or userIn == "r":  #If the user enters R or r then it will enetr remove product mode
        userIn = int(input("Enter group id number.\n")) #Will ask the user to enter the group id number to remove from the excelfile
        del productList[userIn] #Deletes whatever the user entered
    elif userIn == "N" or userIn == "n":    #If the user enters N or n then it will enter new product mode
        userIn = int(input("Enter a grp_id.\n"))    #Will ask the user to enter a new group id number for the new product
        upc7 = int(input("Enter upc7 number.\n"))   #Will ask the user to enter a new upc7 number for the new product
        upc10 = int(input("Enter upc10.\n"))    #Will ask the user to enter a new upc10 number for the new product
        manufacturer = input("Enter manufacturer name.\n")  #Will ask the user to enter a new manufacturer name for the new product
        description = input("Enter description.\n") #Will ask the user to enter a new desciptipon for the new product
        cost = int(input("Enter the cost.\n"))#Will ask the user to enter a new cost for the new product
        productList[userIn] = Product(upc7, upc10, manufacturer, description, cost) #Will take whatever the user input was and put it into product class
    elif userIn == "S" or userIn == "s":    #If the user enters S or s then the program will enter sale mode
        Letter = input("Do you want to add a product?\n")   #Will ask the user if they want to add a product
        runningTotal = 0
        while Letter == "Y" or Letter == "y":  #If the user enters Y or Y then
            userIn = int(input("Enter the id of a product.\n")) #The program will ask the user for the group id number to add the item to the SaleList
            quantity = int(input("Enter a quantity.\n"))    #Will ask the user for how many they want of the item
            SaleList[productList[userIn]] = quantity    #UserIn gets value from productList and uses it for a key in SaleList and usues quantity for a value
            total = productList[userIn].cost * quantity #Will multiply the cost of the item times the quantity
            print(total)    #Will print out the total of the item(s) selcted without the tax
            runningTotal = runningTotal + total #Keeps track of every product added
            Letter = input("Do you want to add a another product?\n")   #Will ask the user if they want to add another product. If the user enters Y or y
                                                                        #then it will go back up to line 46 and will go through the steps to add the item
                                                                        #to your SaleList. When it gets to line 52 again, if you don't want to add another
                                                                        #item then enter any letter and it will bring you back up to line 29 and then that's
                                                                        #when the user would enter T or t to get thier reciept.
    elif userIn == "T" or userIn == "t":    #If the user enters T or t then the program will exit sale mode
        for x in SaleList:  #Calls the quantity, description, and cost from the Product class
            print(str(SaleList[x]) + " " + x.description + "s : " + str(x.cost))
        tax = runningTotal * 0.0625 #The program will calculate the tax by multiplying the runningtotal times 6.25%
        print("The total is", + runningTotal + tax, "plus tax.")    #Will add the total and tax, then print out The total is whatever the cost is plus tax
        break