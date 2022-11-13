class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        
class Cake:
    #can you fill out the rest of this for me? im dumb
    #the cake needs to have the cake flavor and cake frosting stored
    def __init__(self, flavor, frosting):
        self.flavor = flavor
        self.frosting = frosting

class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length
        
        
    def breedGuess(self):
        if self.fur_length == "long":
            return("Domestic Longhair")
        else:
            return("Domestic Shorthair")
            
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        
    #create your own function! what do you want it to do?
    #i want to define tShirt attributes!
class tShirt:
    def __int__(self, size, color, sleeve_length):
        self.size = size
        self.color = color
        self.sleeve_length = sleeve_length
   
def main():
    #fill this one out with a dog's name and age.. can be your dog, friend's dog, etc
    dog1 = Dog("George" , 1)
    print(dog1.name, dog1.age)
    
    #and what about a new employee
    newEmployee = Employee("Bob", 12321, "Finance")
    #how would we print out each of the variables from newEmployee?
    print(newEmployee.name)
    print(newEmployee.idNumber)
    print(newEmployee.department)

    #now create and print out a cake you make
    cake1 = Cake("Vanilla", "Chocolate")
    print(cake1.flavor)
    print(cake1.frosting)
    
    
    #and now create another cake and print it out
    cake2 = Cake("Chocolate", "Cream Cheese")
    print(cake2.flavor)
    print(cake2.frosting)
    
    
    #create a cat!
    cat1 = Cat("Olivia", 10, "long")
    #create another cat!
    cat2 = Cat("Meridith", 8, "short")
    
    #What would we put here to print out the result of breedGuess for cat1?
    print(cat1.breedGuess())
    
    #create a car!
    car1 = Car("Jeep", 2020, "White")
    
    #Now print out the function you made for car :)
    print(car1.model)
    print(car1.year)
    print(car1.color)

main()
