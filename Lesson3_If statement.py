#PART 1 ; CONDITIONAL TEST

cars= ['audi', 'bmw', 'honda', 'toyota']

for car in cars:
    if car=='bmw':
        print(car.title())
    else:
            print(car.upper())
     
#conditional test: 1) checking for equality :  can convert all value to lower before comparing : car='Audi'  car.lower()='audi' -> always true
                  #2) checking for inequality :
requested_topping ='cheese'
if requested_topping != 'mushroom':
    print(" Hold the order!")
#numerical comparison : age=18 age==9-> true
answer= 20
if answer != 30:
    print("It is not the correct answer, please try again!")
                   # you can also put other mathematical comparisons in your code : <,>,<=,>
age=25
if age>18:
    print("you can access to the video")
#multiple conditions:
age_0=25
age_1=20
                   # chú ý chỉ cả hai cái đều pass-> true; chỉ cần at least một cái fail-> false : age_0=19 age_1=17; age_0>18 and age_1>18   ---> false/// age_0>18 and age_1<18 --> true
if age_0>18 and age_1<18:
    print("True")
                   # chú ý dùng mệnh đề "and" nên đúng được chỉ khi cả hai cùng đúng, còn mệnh đề "or" thì chỉ cần một trong hai cái đúng thì mđe đúng, đối vs "or" thì sai chỉ khi cả hai đều sai
#checking whether a value is in a list
requested_topping=['beef','lemon','pepper']
if 'beef' in requested_topping:
    print("yes we have beef")
#checking wether a value is not in a list
banned_users=['maria','sushi','nhimnhim','nhin nhin']
user='lila'
if user not in banned_users:
    print("you can access to our server")
#Boolean expressions : Boolean value is either True or False for ex : game_active= True; can_edit= False,... -> use to track the state of a program or particular condition

#PART 2 : IF-STATEMENT


#if statements:
age=19
if age>=18:
    print("You are old enough")
    print("Have you had an account yet?")
#if-else statements 
age=17
if age>=18:
    print("You are old enough to vote")
    print("Have you had an account yet?")
else:
    print("Sorry! You are not old enough to vote")
    print("Please register to vote as soon as you turn 18!")
#if-elif-else chain: ( use for more than 2 possible situations)            Python executes only one block in the chain, it runs each conditional test until one passes
age=8
if age<4:
    print("your fee is $0")
elif age<18:
    print("your fee is $5")
else: 
    print("your fee is $10")
         #2nd way
if age<4:
    price=0
elif age<18:
    price=5
else:
    price=10
print("your entrance fee is $"+ str(price)+".")
#multiple elif Blocks:
if age<4:
    price=0
elif age<18:
    price=5
elif age<65:
    price=10
else:
    price=5
print("your entrance fee is $"+ str(price)+".")
#obmitting the else Block in the if-elif Chain : Python does not need the else Block in this kind of chain, sometimes removing the else Block and use instead an additional elif-statement to catch the specific condition of interest
if age<4:
    price=0
elif age<18:
    price=5
elif age<65:
    price=10
elif age>=65:
    price=5
print("your entrance fee is $"+ str(price)+".")
#test multiple conditions : if-elif-else only use for one test ( to pass)( when Python find one test that passes-> it skips the rest conditions, other cases
#that needs testing all the conditions -> using multiple simple if-statements
requested_topping=['beef','chilli','pepper','onion']
if 'mushroom' in requested_topping:
    print("Adding mushroom")
if 'candy' in requested_topping:
    print("Adding candy")
if 'chilli' in requested_topping:
    print("Adding chilli")
if 'onion' in requested_topping:
    print("Adding onion")
print("Finishing your pizza order!")
              #lỗi sẽ xảy ra nếu dùng hàm if-elif(-else) chain vì nó sẽ skips các conditions sau once Python finds the one test passing, like this :
requested_topping=['beef','chilli','pepper','onion','mushroom']
if 'mushroom' in requested_topping:
    print("Adding mushroom")
elif 'candy' in requested_topping:
    print("Adding candy")
elif 'chilli' in requested_topping:
    print("Adding chilli")
elif 'onion' in requested_topping:
    print("Adding onion")
print("Finishing your pizza order!") #nó đã skip hết các conditions sau condition đầu tiên vì test passes through first condition
#Using if statement with a list:
#checking for special item: ( ex : check 1 test thôi, check nhiều test thì dùng multiple if )
requested_toppings=['pepper','chilli','lemon','beef']
for requested_topping in requested_topping:
    if requested_topping=='lemon':
        print("Sorry we are run out of lemon")
    else:
        print("Adding "+ requested_topping+".")
print("finishing you pizza order!".title())
#checking that a list is not empty
print("new task")
#dòng if+ tên list: -> nếu list có chứa elements
requested_ingredients=[]
if requested_ingredients:
    for requested_ingredient in requested_ingredients:
        print('Adding'+requested_ingredient+".")
else:
    print("Are you sure for ordering a plain pizza?")
#using multiple lists:
requested_toppings=['pepper','chilli','lemon','beef']
available_toppings=['beef','meat','onion','lemon']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding "+requested_topping+'.')
    else:
        print("We are run out of "+requested_topping+" "+".Sorry!")

    



    




















    

            
