food = {"Banana": 5}
print(food)
userIn = input("Enter a key 'is/are' value").split()
food[userIn[0]] = userIn[2]
print(food)
