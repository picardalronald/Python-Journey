# Practice OOP

# child class with an object and properties
class Personal:
    # initialization for those objects
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def greetings(self):
        print(f"What your name? : {self.name}")
        print(f"How old are you? : {self.age}")
        print(f"What your gender? : {self.gender}")
        


# inherit in parent class
class Ronald:
    def __init__(self, name, lastname, age, gender, ):
     self.name = name
    #  Private oject using encapsulation
     self.__lastname = lastname
     self.age = age
     self.gender = gender
     
    def greetings(self):
        # private object can access
        print(f"Hello sir {self.name + " " + self.__lastname}")
        print(f"Your are {self.age} Yrs old right")
        print(f"Are your {self.gender}")
    
# pass the value of object here         
ron = Ronald("Ronald", "Picardal", 21 , "Male")     

# user input
# names = input("Enter your name: ")
# ages = input("Enter your age: ")
# genders = input("Enter your gender: ")

# this is an object
# result = Personal(names, ages, genders)

# print result here 

# print("\nHere the list of Question:")
# result.greetings()

# print result here 
print("\nHere the list of your Information:")
ron.greetings()


        
        
        
