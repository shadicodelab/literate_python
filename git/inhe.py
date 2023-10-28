class mammal:#parent class created
    def walk(self):#creating a method walk for the parent class 
        print("walk")
        
class dog(mammal):#crating the child class
    def bark(self):#method specific to the sub_class
        print('bark')

class cat(mammal):
    pass#this statement is used when a class does not hae a specific method

dog1 = dog()#creating an object for the methods
dog1.walk()#calling the object which calls the method of parent class
dog1.bark()
