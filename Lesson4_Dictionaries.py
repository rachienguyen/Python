#SIMPLE DICTIONARIES
alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

#WORKING WITH DICTIONARIES
#Dictionary is a collection of key-value pairs. Each key is connected to a value and you can use a key to access the value associated with that key.
                                            # A key's value can be : number, string, list, another dictionary
                                            # Dictionary is wrapped in the braces, {all the key-value pairs inside}
#Accessing Values in a Dictionary: to get to the value associated with a key:
alien_0={'color':'red','points':10}
print(alien_0['color'])
new_points=alien_0['points']
print("You have earned "+str(new_points)+" points.")
#Adding new key-value pairs
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)
#Starting with an empty dictionary
alien_1={}
alien_1['name']='Jack'
alien_1['age']=38
print(alien_1)
#Modifying values in a dictionary: change the value of key
alien_0={'color':'green'}
alien_0['color']='yellow'
print("The alien is now "+ alien_0['color'])
     #Move the alien to the right
     #Determine how far to move the alien based on its current speed
alien_0={'x_position':'0','y_position':'25','speed':'medium'}
print("Original x-position: "+str(alien_0['x_position']))
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
elif alien_0['speed']=='fast':
     x_increment=3
alien_0['x_position']=alien_0['x_position']+ str(x_increment)
print("New x-position is "+ str(alien_0['x_position']) +" .")
#Removing key-value pairs(remove permanently):                                               using del
alien_0={'color':'red','points':10}
del alien_0['color']
print(alien_0)
#A dictionary of similar objects : same kinds of information but for many objects:
favourite_language={
    'jen':'python',
    'jupiter':'C',
    'linda':'C++',
    'Min':'R'}
print("jupiter's favourite language is "+ favourite_language['jupiter'].upper()+" .")

#LOOPING THROUGH A DICTIONARY:
#Looping through all key-value pairs
user_0={
    'username':'emily',
    'first':'ema',
    'last':'brown'
    }
           #Loop thru the dictionaries using methods:                   _____.items()
for k,v in user_0.items(): #____.items methods returns a list of k-v pairs (.items() -> key-value)
    print("\nKey: "+k)
    print("\nValue: "+v) # sometimes they key-value pairs are not returned in the order in which they were stored, Python tracks only the connections between individuals keys and their values 
favourite_language={
    'jen':'python',
    'jupiter':'C',
    'linda':'C++',
    'Min':'R'}
for name,language in favourite_language.items():
    print("\n" +name.title()+"'s favourite language is: "+language.upper())
#Looping through all the keys:
favourite_language={
    'jen':'python',
    'jupiter':'C',
    'linda':'C++',
    'Min':'R'}
print("New taskkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
for name in favourite_language.keys():                    #.keys()or nothing-> keys ( nothing because looping thru the keys is actually the default behaviour when looping thru dictionary)
    print(name.title())
for name in favourite_language:
    print(name.upper())

friends=['peter','linda']
for name in  favourite_language:
    if name in friends:
        print("Hi "+name.title()+", I see your favourite language is "+ favourite_language[name].title()+" !")
for friend in friends:
    if friend not in favourite_language.keys():
        print("Hi "+friend.title()+". Please take out poll!")
#Looping thru keys in order:(alphabet order) sorted(___)
favourite_language={
    'jen':'python',
    'jupiter':'C',
    'linda':'C++',
    'min':'R'}
for name in sorted(favourite_language.keys()):
    print(name.title()+ ", thank you for spending time taking out the poll!")
#Looping thru all values:
favourite_language={
    'jen':'python',
    'jupiter':'C',
    'linda':'C++',
    'min':'R',
    'Henla':'R'}
print("The following languages have been mentioned:")
for language in favourite_language.values():
    print(language.title())
print("new task")
            #get rid of repetitive values, we use       set()
for language in set(favourite_language.values()):
    print(language.upper())

#NESTING:
#A list of dictionaries:
alien_0={'color':'red','points':10}
alien_1={'color':'green','points':15}
alien_2={'color':'yellow','points':20}

aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

aliens=[]
for alien_number in range(30): #range() tells Python how many times we want the loop to repeate
    new_alien={'color':'green','points':'5','speed':'slow'}
    aliens.append(new_alien)
    #showing the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")

aliens=[]
for alien_number in range(0,30):
    new_alien={'color':'yellow','points':'5','speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10
    elif alien['color']=='yellow':
         alien['color']='red'
         alien['speed']='fast'
         alien['points']=15
for alien in aliens[0:5]:
    print(alien)
print("...")
#A list in dictionaries
pizza={
    'crust':'thick',
    'toppings':['mushroom','extra cheese']
    }
print("You ordered a "+pizza['crust']+"-crust pizza "+"with the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)

    
favourite_language={
    'jen':['python','java'],
    'jupiter':['C','C++'],
    'linda':['C++'],
    'Min':['R','Python']
    }
for name,languages in favourite_language.items():
    print("\n"+name.title()+"'s favourite language are:")
    for language in languages:
        print("\t"+language.title())

#A dictionary in dictionary
users={
    'aestein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
        }
    } #big dicitionary "users" has two little dictionaries: 'aestein' and 'mcuries' ( name of two small dictionaries), dùng dấu : thay cho dấu bằng đối với small dicts in a big main dict
for username,user_infor in users.items(): 
    print("\nUsername: "+username)
    full_name=user_infor['first']+" "+user_infor['last'] #username,user_infor are now relatively name of dictionaries and infor in dictionaries #cái user_infor là một dictionary nhỏ bên trong lại chứa 3 keys : first,last,location
    location=user_infor['location']

    print("\tFull name : "+full_name.title())
    print("\tLocation: "+location.title())







    

    
    

                                        
