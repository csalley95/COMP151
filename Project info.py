dictionary = {"apple":2,"banana":3}

del dictionary["apple"]
print(dictionary)

class Rectangle:
    def __int__(self, color, length, width):
        self.color = color
        self.length = length
        self.width = width
        self.quantity = 0
    def toString(self):
        print(self.name + " is a " + self.color +
              self.length + " by " + self.width +
              "rectangle")
    def setName(self, name):
        self.name = name
    def setQuantity(self, amount):
        self.quantity = amount


userIn = input("Enter the color, length, and width")