#Gradebook

class student:
    def __init__(self,firstname,lastname,id): #constructor
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.assignmentlist = []

    def addassignment(self,assignment):
        #common- error checking assignment here
        self.assignmentlist.append(assignment)

    def calculateaverage(self):
        average = self.runningtotal() / len(self.assignmentlist)
        return average

    def runningtotal(self):
        total = 0
        for i in self.assignmentlist:
            total = i + total
        return total

class GradeBook:
    def __init__(self):
        self.studentlist = []

    def addstudent(self,student):
        self.studentlist.append(student)

    def printtallscores(self):
        for i in self.studentlist:
            print(i.firstname + " " + i.lastname + " " + str(i.calculateaverage()))

tempstudent1 = student("Bob","Smith",1)
tempstudent2 = student("Jane","Doe",2)

tempstudent1.addassignment(80)
tempstudent1.addassignment(95)
tempstudent2.addassignment(85)
tempstudent2.addassignment(95)

studentgradebook = GradeBook()
studentgradebook.addstudent(tempstudent1)
studentgradebook.addstudent(tempstudent2)
studentgradebook.printtallscores()