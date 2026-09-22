print("hello. welcome to data structures class !!!")

number1 = 10;
print(f"var number1 is: {type (number1)}")

gravity = 9.8;
print(f"var gravity is: {type (gravity)}")

numberx = 8j
print(f"var numberx is: {type (numberx)}")

#string Data Types
my_name = "Johan"
fullname = 'peter McDonald'
description = '''
      Hello, how's it going?
      This is amazing !!!
      '''



week_days = []
print(week_days)
print(type(week_days))

fruits = {}
print(fruits)
print (type(fruits))

months = ()
print(months)
print(type(months))

personal_info =[
    'Johan',
    'Ayala',
    50,
    True,
    '3183219939',
    'Pasto',
     ['Juli',9]
]
print(personal_info)
# Show father age and city
print(f"father age : {personal_info[2]}")
print("father city : ",personal_info[5])
print(f"Daugther age : {personal_info[6][1]}")

#Update modificar la edad del padre 
new_age = input("please, type the new father age:")
personal_info[2] = new_age
print(f"new father age is: {personal_info[2]}")

#add new information
personal_info.append('malala')
print(personal_info)

#Tuple 
user_data= ('julieth ','Romo')
print(user_data)