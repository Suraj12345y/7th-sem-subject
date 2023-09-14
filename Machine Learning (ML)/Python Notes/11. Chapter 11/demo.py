# class Employee:
#     company="Google"
    
#     def showDetails(self):
#         print("this is a employee class")

# class Programmer(Employee):
#     company="Microsoft"
#     language="Python"

#     def showLanguage(self):
#         print(f"Language is{self.language}")

#     def showDetails(self):
#         print("this is a programmer class")

# a=Employee()
# a.showDetails()
# p=Programmer()
# p.showDetails()
# print(p.company)
########################################################

class Animal:
    pass

class pet(Animal):
    pass

class Dog(pet):
    
    @staticmethod
    def bark():
        print("Dog is barking")

a=Dog()
a.bark()
    
    
