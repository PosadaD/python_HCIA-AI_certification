#What is object oriented programing?
#oop is a program paradigm that organizes software design around objects, instead of funtions and logic.

#Class and object 
#An object is a collection of data and methods that act on those data
#A class is a blueprint for an object

#Encapsulation 
#Inheritance
#Abstraction
#Polymorphism


#create a class that simulates a dog
class Dog():
    def __init__(self, name, age):
        self.name = name;
        self.age = age;

    def sit(self):
        print(self.name.title()+"is now sitting")
    
    def run(self):
        print(self.name.title()+"is now running")

#instantation
my_dog = Dog("willy", 5);
my_dog.sit();
my_dog.run();

#add new data to an object 
my_dog.food = "dog food";
print(my_dog.food);

#re-define a class
