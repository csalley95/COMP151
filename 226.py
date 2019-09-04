from tkinter.filedialog import askopenfilename

infile = askopenfilename()
file = open(infile, "r")
line = file.readline()
listofnum = line.split(',')
print(listofnum)

total = 0
loopcounter = 0

for i in listofnum:
    i = int(i)
    total = total + i
    loopcounter = loopcounter + 1
mean = total / loopcounter
print("The mean of your number is " + str(mean))
