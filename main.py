import Database
import Menulib
"""
Project : KnowT - Ultimate Portal for Teachers 
Author : Anjali Gupta
"""

def login():
    print("\t\t\tKnowT - Ultimate Portal for Teachers\n")
    user_name = input("Enter username: ")
    password = input("Enter password: ")
    response = Database.Authenticate(username=user_name, password=password)
    if response == True :
        print(f"\t\t\tAuthentication Sussesfull! Welcome {user_name}")
    else :
        print(f"\t\t\tAuthentication Failed!")
        welcome()


def welcome():
    print("\t\t\tKnowT - Ultimate Portal for Teachers\n")
    print("1. Login")
    print("2. New User? Register ")
    choice = int(input("Enter Choice: "))

    while choice!=0:
        if choice == 1:
            login()
            break

        elif choice == 2 :
            Database.Register()
            welcome()
            break        

        elif choice == 0:
            print("Exiting...")
            break
        
        else:
            print("Wrong Choice.....Enter Your Choice again")
            choice = int(input("Enter Choice again: "))

def setup():
    Database.DatabaseCreate(database_name='KNOWT')
    Database.TablesCreate()

def start():
    Menulib.MainMenu()
        

if __name__ == "__main__" :
    setup()
    welcome()
    start()



