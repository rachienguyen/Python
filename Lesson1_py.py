#Lesson1:
#CHAPTER 1,2
#PART I
#simple_program
print("Hello Python World")
#variable
message= "Hello Python World!"
print(message)
#Naming and using Variables
message_1= "Running man"
print(message_1)
#Avoiding name error when using variables : ex :
##message= "Hi"
##print(masage)


#PART II
#STRING
"this is a string"
'this is a string'
'I told my friend, " Going out for Easter with me "'
#changing Case in the string with methods
name= "lim lace"
print(name.title())
print(name.upper())
print(name.lower())
#combining or concatenating strings
first_name= "lim "
last_name= "lace"
full_name= first_name.title() + last_name.title()
print(full_name)
print("Hello, " + full_name + "!")
#Adding white space to strings by using Tabs(\t) or Newlines(\n)
print("python")
print("\tPython")
print("My name : \nLim \nLace")
#stripping whitespace(loai bo whitespace)
favourite_language= "python "
print(favourite_language.rstrip())

favourite_language= " Java"
print(favourite_language.lstrip())

favourite_language= " Java "
print(favourite_language.strip())
#avoiding syntax errors with strings
#chu y Single Quote should use only for 1 character or use together with Double quote
#it can not use as a string.
message="one of the strengths of python is its community"
print(message)
# wrong: message='one of the strengths is community'
message=' one of the strengths of python is "community" '
print(message)


#PART III : NUMBERS : you can plus, minus, multiply, divide in Python : +,-,*,/
#1 : Float : Python calls any number with decimal point a "float" -> should use decimal without worrying about how they behave
print( 5 + 3 )
print( 5.0 / 3 )
#! sometimes you will get abitrary number in your answer like this : 0.300000000000000000004 -> just ignore, it normal
print( 0.2 + 0.1 )
# age= 23
# message= " Happy " + age + "rd Birthday" -> you might expect the result will be like Happy 23rd Birthday but no, there will be mistake of not running because age=23 is a varible has interger value but Python does not know how to interpretate it, it can present either 2 3 as characters or 23 as numerical value, so use str() function to present non-string value as a string
age= 23
message= "Happy" + str(age) + "rd Birthday !"
print(message)
#Zen Python -> fonnnnnnnn
import this 





#CHAPTER 3 : INTRODUCTING LISTS
# A list is a collection of items in a particular order. [ ] - represents 'list' and elements are seperated by comma ","
bicycles = [ 'trek', 'cannondale', 'redline']
print(bicycles)
#assessing elements in a list : [0]-first element; [1]-second element; [2]-third element,...; [-1]-last element in the list, second last in the list [-2],...
print(bicycles[0].upper())
print(bicycles[-2].title())
#using individual value from the list
message= "My first bycicle was a" + " " + bicycles[-1].title() + "."
print(message)
#changing, adding, and removing elements
flowers= [ 'rose', 'violet', 'tuylip' ]
flowers[-1]='daisy'
print(flowers)
#adding
#add 1 : appending elements to the end of list; using             .append(   )
flowers.append ('lotus')
print( flowers)
#add 2 : inserting elements into the list : you can use           .inset( no. , )
flowers.insert(0,'mini daisy')
print(flowers)

#removing
#remove 1 : remove elements from a list : using det statement ( one delete, cannot recover)                                     del    _____[ no. ] 
del flowers[0]
print(flowers)
#remove 2 : remove elements using pop() Method, pop one items off the top of the stack -> remove the last item popped_.....= ......pop()
#...: (one remove can still use)                         popped_.....= ......pop() -> .....pop() nghĩa là remove cái item cuối, còn popped_... là cái item bỏ đi
print("Looking at thissssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
popped_flowers= flowers.pop()
print(flowers)
print(popped_flowers)

vehicles=['car', 'bicycle', 'truck']
popped_vehicles= vehicles.pop(0)
print(vehicles)
print(popped_vehicles)
#remove 3 : pop any items from any position in a list : chỉ cần thêm số vào pop(no) ex : .pop(1), pop(0),...
vehicles=['bus', 'metro', 'tram']
popped_vehicles= vehicles.pop(0)
print(vehicles)
print(popped_vehicles)
print(" I normally go to school by " + " " + popped_vehicles.upper())
#remove 4 : if you do not know the position but knowing the value: using remove() Method                                   .remove(  )
too_cheap= 'metro'
too_expensive= 'bus'
vehicles.remove(too_cheap)
print(vehicles)
#way 1 : remove luôn
Point_class= [ 'one', 'two', 'three' ]
Point_class.remove('one')
print(Point_class)
#way 2 : remove và lưu lại giá trị removal
Point_class= [ 'one', 'two', 'three' ]
Low_point= 'two'
Point_class.remove(Low_point)
print(Point_class)

#Organizing a List
#sorting a list permanently by sort() Method
cars= ['audi', 'ducati', 'bmw', 'canya']
#classical sort() : in alphabetical order                                                 .sort() -> alphabet order
cars.sort()
print(cars)
#reverse alphabet order using sort(reverse= True)                                         .sort(reverse= True)-> reverse alphabet order
cars= ['audi', 'camri', 'ducati', 'bmw']
cars.sort(reverse= True)
print(cars)

#sorting temporarily a list with sorted() function                                          print(sorted(___)) ;  print(sorted(____,reverse= True))
cars= ['audi', 'camri', 'ducati', 'bmw']
print("Here is the original list : ")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the sorted list but in reverse alphabetical order:")
print(sorted(cars,reverse= True))

print("\nHere is the original list again:")
print(cars)
#!!!! Sorting a list alphabetically will be difficult if elements are not in lowercase

#Print a list in REVERSE order < not alphabetcally reverse >                                _____.reverse()
cars= ['audi', 'camri', 'ducati', 'bmw']
cars.reverse()
print(cars)
#Find length of the list                                                                    print(len(_____))
cars= ['audi', 'camri', 'ducati', 'bmw']
print(len(cars))
#Avoiding Index Errors when working with Lists
#1 asking for wrong item , having only 3 but ask for the forth one
#2 [-1] is always the last item-> always true. Only wrong when calling for [-1] in empty list like motocycle=[ ]










