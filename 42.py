#1 Read lines of file
    #For each line, add product to a dictionary

from tkinter.filedialog import askopenfilename
filename = askopenfilename()
fileObject = open(filename, "r")
filelines = (fileObject.readlines())
productList = {}

class Product:
    def __init__(self,upc7,upc10,manufacturer,description,cost):
        self.upc7 = upc7
        self.upc10 = upc10
        self.manufacturer = manufacturer
        self.description = description
        self.cost = cost


for x in filelines:
    product = x.split(',')
    tempproduct = Product(product[1],product[2],product[3],product[4],float(product[5][0:-1]))
    productList[int(product[0])] = tempproduct


ARlist = {}
run = True
Letter = " "
while run == True:
    userIn = input("Please enter a letter.\n")
    if userIn == "R" or userIn == "r":
        userIn = int(input("Enter group id number.\n"))
        del product[userIn]
    elif userIn == "N" or userIn == "n":
        userIn = int(input("Enter a grp_id.\n"))
        upc7 = int(input("Enter upc7 number.\n"))
        upc10 = int(input("Enter upc10.\n"))
        manufacturer = input("Enter manufacturer name.\n")
        description = input("Enter description.\n")
        cost = int(input("Enter the cost.\n"))
        productList[userIn] = Product(upc7, upc10, manufacturer, description, cost)
    elif userIn == "S" or userIn == "s":
        Letter = input("Do you want to add a product?\n")
        runningTotal = 0
        while Letter == "Y" or Letter == "y":
            userIn = int(input("Enter the id of a product.\n"))
            quantity = int(input("Enter a quantity.\n"))
            ARlist[productList[userIn]] = quantity
            total = productList[userIn].cost * quantity
            print(total)
            runningTotal = runningTotal + total
            Letter = input("Do you want to add a product?\n")
    elif userIn == "T" or userIn == "t":
        for x in ARlist:
            print(str(ARlist[x]) + " " + x.description + "s : " + str(x.cost))
        tax = runningTotal * 0.0625
        print("The total is ", + runningTotal + tax)
        break

