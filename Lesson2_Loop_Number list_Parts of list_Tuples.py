#CHAPTER 4:
#LOOP WITH A LONG LIST

#1 Using a For Loop to avoid repetitive action for each elements in a list
#            step 1: define a list ; step 2: define a FOR loop; step 3: define action ex: print,...                                       for ____ in ____s :   
#            chú ý dòng action phải bị indented ( cách đầu dòng ) because Python uses indentation to determine when one line of code is connected to the line above it. 
magicians = ['alice', 'david', 'carolina']
for magician in magicians :
  print(magician)
print("Thank you all for your attention!!")
#2 Common mistake of inđentation missing :
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(magician.title() + ", that was a great trick!")
 # Nếu để câu lệnh hai thụt vào như này nó sẽ chỉ output cho ra element cuối cùng của list chứ không chạy lệnh của loop. 
print("I can't wait to see your next trick, " + magician.title() + ".\n")
 # Cho indentation không đúng chỗ, k cần thiết-> Python sẽ báo sai
 # Cho indentation không đúng chỗ trong For loop mà không cần dùng tới For loop -> code will be repeated once for each item in the list.
magicians = ['alex', 'david', 'carolina']
for magician in magicians:
 print(magician.title() + ", that was a great trick!")
 print("Thank you for your shows")
#Colon : ( dấu hai chấm) sau For loop dùng để tell Python to interpret the next line as the start of a loop. -> nếu bỏ sót nó Python sẽ báo lỗi




#MAKING NUMERICAL LIST
 
#1 a) using a range function                                                                    range() function 
for value in range(1,5) :
    print(value)
# OBOE( Off-by-one error )- lỗi khuyết đi giá trị cuối 0<=x<5 = range(0;5) -> chỉ print 0,1,2,3,4 , hệ quả của off-by-one behaviour


#  b) using range function to make a list of number
numbers= list(range(6))
print(numbers)
#  b.1) Cách list ra even_number : viết list(range(a,b,2)) nghĩa là nó sẽ list ra các giá trị xuất phát từ 2 và cộng thêm 2 đơn vị vào số tiếp theo tới khi nó reach max=b
even_numbers= list(range(0,6,2))
print(even_numbers)
#  b.2) Cách list ra squares : 1-tạo hàm list; 2-tạo For loop; 3-viết công thức cho mỗi giá trị trong hàm list; 4-gán giá trị trong hàm với hàm; 5-action
#  b.3) cách 2 nhanh hơn : 1-tạo hàm list; 2-tạo For loop; 3- gán giá trị trong hàm với hàm trực tiếp; 4-action
squares=[]
for value in range(1,15):
    square= value**2
    squares.append(square)
print(squares)

squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

#2 Simple statistics function with list of numbers
print(min(range(9)))
print(max(range(9)))
print(sum(range(6)))

digits= [2,4,5,6,8,9]
print(min(digits))
print(max(digits))
print(sum(digits))
#List comprehension using for shorten the code for print the squares of list of number value
squares=[ value**2 for value in range(1,11)]
print(squares)

#WORKING WITH A PART OF A LIST

#you used learn how to work through single element and all elements in the list, now you will have to work with a specific group of items in the list
#Python call this "SLICE"-specific group of items in the list
#1  Slicing a list :                                                                                      print(__[index number : index number ]) (: means to)
#to make a slice, you specify the index of the first and last elements you want to work with. Alike to range() function, it has OBOE, if you want to output the first three elements in a list you need to request indices 0-3(0 as first,1 as second,2 as third)
friends=["Aapali","Hassan","Yunwoo","Tatsuki","Eli","Hana"]
print(friends[0:6])
print(friends[:6])
print(friends[2:])
# -> print(friends[-1]) in ra số đầu tiên từ cuối lên, k theo quy tắc bắt đầu từ 0 :)) 
# print(friends[-3:-1]) vẫn tuân theo quy tắc OBOE ( số cuối phải cộng thêm 1 cho cả âm hay dương ), chú ý nó chỉ print từ trái qua phải, k in ngược lại 
print(friends[-3:-1])
print(friends[-3:])
#2 Looping through a slice
animals=["cat",'dog','duck','fish','frog']
print("Here is the animals that i think they are cute:")
for animal in animals[:3]:
  print(animal.upper())
#2 Copying a list                                              using [:]
my_foods=['cheese','berry','chocolate','coffee']
my_friend_foods=my_foods[:]
print("My friend's favourire foods are:")
print(my_friend_foods)
#ở đây mình dùng [:] thay vì dùng đơn giản cho hai list bằng nhau vì dùng [:] thể hiện sự copy ở thời điểm đó của một biến theo biển kia và hai biến sau thời điểm đó
#tách biệt-> sự thay đổi sau đó của mỗi biến là k liên quan tới nhau, nêu mình gán cho chúng bằng nhau thì thay đổi một biển thì biến kia cx thay đổi
my_friend_foods.append('chicken wings')
my_foods.append('soda')
print(my_friend_foods)
print(my_foods)

#TUPLES
#1 Defining a Tuple : Tuple like a list but their element's values are immutable ( cannot change ), and we use parenthese( ngoặc đơn)
#instead of square brackets[ngoặc vuông]
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
#let see what happens if we change one of the items in the tuple -> Python will tell us we can not assign new value to an iteam in tuple
#2 Looping thru all values in a tuple : You can loop over all values in a tuple as you did with a list
for dimension in dimensions:
  print(dimension)
#3 Writing over a tuple : we can not modify a tuple but we can assigning a new value to a variable in a tuple by redefining the entire tuple ( creating new tuple)
print(" old dimensions:")
dimensions=(200,50)
for dimension in dimensions:
    print(dimension)
print("modified dimensions:")
dimensions=(210,50)
for dimension in dimensions:
    print(dimension)
                       #use tuple for storing a set of values that can not be changed thru out the life of a program
     
#STYLING YOUR CODE : Some elementary rules 
# Rule 1 : Use 4 spaces/indentation level ( space is space, do not use mix of tab and space )
# Rule 2 : PEP 8 Guildlines suggest limiting your comments to 72 characters/line
# Rule 3 : To group parts of your program visually and also use blank lines to organize your files. Ex : you have 5 lines to build a list then
           #another 3 lines to do sth with that list. It's appropriate to put a blank line between two sections. But do not use two much blank lines that
           #are not neccessary -> to be more readable.















 

