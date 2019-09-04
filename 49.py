class car:
    def __init__(self,price,year,make,model):
        self.year = year
        self.make = make
        self.model = model
        self.price = price
        self.mileage = 0
        self.fuelLvl = 10
        self.DTOC = 10000

    def drive(self,miles):
        self.miles = self.mileage + miles
        self.DTOC = self.DTOC - miles
        self.fuelLvl = self.fuelLvl - (miles/100)

    def gas(self,fuelLvl):
        self.fuelLvl = 10

    def oilChange(self):
        self.DTOC = 10000
cara = car(2011, 'Toyota','Corolla',20000)
cara.drive(5000)
