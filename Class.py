class Dog(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name.title()+ " is sitting. ")
    def roll_over(self):
        print(self.name.title()+" is rolling over!") 
#Creating multiple instances for the class instruction
my_dog=Dog("Willie",6)
print("My dog's name is "+my_dog.name.title())
print("My dog is "+str(my_dog.age).title())
your_dog=Dog("Holly",8)
print("Your dog'name is "+your_dog.name.title())
print("Your dog'age is "+str(your_dog.age))
#Calling methods defined in the class with multiple instances
my_dog.sit()
your_dog.roll_over()

#Try it yourself
class Restaurant(object):
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("The restaurant'name is "+self.restaurant_name.title()+"and its cuisine type is "+self.cuisine_type.title()+".")
    def open_restaurant(self):
        print(self.restaurant_name.title()+" is opening.") 
your_restaurant=Restaurant("Kaggle","Thai")
my_restaurant=Restaurant("Vincent","desert")
your_restaurant.describe_restaurant()
my_restaurant.describe_restaurant()

class User(object):
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def describe_user(self):
        print("User's name is "+self.first_name.title()+" "+self.last_name.title())
    def greet_user(self):
        print("Hello "+self.first_name.title()+" "+self.last_name.title())
user_one=User("Alex","Durak")
user_two=User("Brocoli","Mulli")
user_one.describe_user()
user_one.greet_user()
user_two.describe_user()
user_two.greet_user()


    

