class Person:
    def __init__(self,first,last,dob):
        self.first = first
        self.last = last
        self.dob = dob
        self.state = 'MA'

    def print_info(self): #Polymorphism
        print("{0} {1} was born on {2} and is currently in {3}".
              format(self.first,self.last,self.dob,self.state))

class Employee(Person): #Inheritance from person
    def __init__(self,first,last,dob,state,id):
        Person.__init__(self,first,last,dob)
        self.state = state
        self.id = id
        self.hoursworked = 0
        self.vacationhoursleft = 40
        self.vacationdestinations = []
    def add_hours(self,hours):
        self.hoursworked = self.hoursworked + hours
    def Reset_Hours(self):
        self.vacationhoursleft = 40
    def take_vacation(self,hours,TravelDestination):
        self.vacationhoursleft = self.vacationhoursleft - hours
        if (TravelDestination in self.vacationdestinations):

        else:
            self.vacationdestinations.append(TravelDestination)
        self.vacationdestinations.append(TravelDestination)
    def print_info(self):
        Person.print_info(self)
        print("{0} {1} worked {2} hours and took vacation and has {3} hours left"
              .format(self.first,self.last,self.hoursworked,self.vacationhoursleft,self.vacationdestinations))

tempPerson = Employee("Bob","Smith","01/01/1990","MA",1)
tempPerson.add_hours(8)
tempPerson.take_vacation(6,)
tempPerson.print_info()

tempPerson2 = Person("Jane","Doe","01/01/1990")
tempPerson2.print_info()