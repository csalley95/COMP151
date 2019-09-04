from tkinter.filedialog import askopenfilename

filename = askopenfilename()
tempfile = open(filename, "r")
print("output of read: ", tempfile.readline())
tempfile.close()
tempfile = open(filename, "r")
print("output of readline: ", tempfile.readline())
tempfile.close()
tempfile = open(filename,"r")
print("output of readlines: ", tempfile.readline())
tempfile.close()
