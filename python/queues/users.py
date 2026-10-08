import os
from datetime import date
#funciones
def mainMenu():
    print(":::::MainMenu::::")
    print("[1].Register a new user")
    print("[2].List all users")
    print("[3].Search user")
    print("[4].Deleteusers")
    print("[5].Update users")
    print("[6].Show active users")
    print("[7].Show inactive users")
    print("[8].Exit")
ids = []




statuses = []
created_at = []

#menu
while True:
    os.system('clear')
    mainMenu()
    opt = input ('Press amy option[1-8]:')
    match opt:
        case '1':
              os.system('clear')
              print("::::Register form:::")
              id = input("Ident number:")
              firstname = input ("Ident number:")
              lastname = input ("lastname")
              mobile_phone = input ("mobile phone")
              email = input ("Email")
              gender = input ("gender [M/F/O]:")

              ids.append(id)
              ids.append (firstname)
              ids.append(lastname)
              ids.append(mobile_phone)
              ids.append(email)
              statuses.append(True)
              ids.append(genders)
              created_at.append(date.today())
              print("users has been created succesfolly!!")
              any_key = input ("press any key to look to9 main menu ")
        case '2':
              print("list all registered users:")

            
    
    