import mysql.connector
import mysql
import time
connection = mysql.connector.connect(user="root",database="bank",password="ASDRL6644dl")
#conection.close()
cursor = connection.cursor()




def signup(): 
    accountuser = input(str("please input a name ")) 
    
    accountpin = input(("please input a pin "))
    addaccount = ('insert Into account (accountname, idaccount,accountbalence) VALUES (%s,%s,%s)')
    cursor.execute(addaccount, (accountuser,accountpin,0))

 
    for item in cursor:

        print(item)
        connection.commit()
        print("you have succecfully signedup")
    while True:

        print(f'''--------hello {accountuser} what would you like to do --------
          1:check balence
          2:add balence
          3:delete account
          4:logout
--------------------------------------------------------------------------------
          ''')
        sigh_choice = int(input("Pick your number: "))
    
        if sigh_choice == 1:
            cursor.execute("SELECT accountbalence FROM account WHERE accountname = %s", (accountuser,))
            balance = cursor.fetchone()
            if balance:
                print(f"You have {balance[0]} dollars")
                time.sleep(2)
            else:
                print("Unable to retrieve balance.")     
                time.sleep(2)

        elif sigh_choice == 2:
            amount = float(input("Enter the amount to add to your balance: "))
            cursor.execute("UPDATE account SET accountbalence = accountbalence + %s WHERE accountname = %s", (amount, accountuser))
            connection.commit()
            print(f"Added {amount} to your balance.")
            time.sleep(2)

        elif sigh_choice ==3:
                confirm = input("Are you sure you want to delete your account? (yes/no): ")
                if confirm.lower() == 'yes':
                    delete_query = "DELETE FROM account WHERE accountname = %s"
                    cursor.execute(delete_query, (accountuser,))
                    connection.commit()
                    print("Your account has been deleted.")
                    break  
                else:
                    print("Account deletion canceled.")
                    time.sleep(2)
        elif sigh_choice ==4:
                print("logged out")
                time.sleep(2)
                startup()
        else:
            print("invalid choise try again but pick a number between 1-3")
            time.sleep(2)
def login():
    username = input("Enter your username: ")
    pin = input("Enter your pin: ")
    query = "SELECT * FROM account WHERE accountname = %s AND idaccount = %s"
    cursor.execute(query, (username, pin))
    results = cursor.fetchall()
    if results:
        print("You logged in")
        while True:

            print(f'''--------hello {username} what would you like to do --------
          1:check balence
          2:add balence
          3:delete account
          4:logout
--------------------------------------------------------------------------------         
          ''')
            log_choice = int(input("Pick your number: "))
    
            if log_choice == 1:
                cursor.execute("SELECT accountbalence FROM account WHERE accountname = %s", (username,))
                balance = cursor.fetchone()
                if balance:
                    print(f"You have {balance[0]} dollars")
                    time.sleep(2)
                else:
                    print("Unable to retrieve balance.")
                    time.sleep(2)     
            elif log_choice == 2:
                amount = float(input("Enter the amount to add to your balance: "))
                cursor.execute("UPDATE account SET accountbalence = accountbalence + %s WHERE accountname = %s", (amount, username))
                connection.commit()
                print(f"Added {amount} to your balance.")
                time.sleep(2)
            elif log_choice ==3:
                confirm = input("Are you sure you want to delete your account? (yes/no): ")
                if confirm.lower() == 'yes':
                    delete_query = "DELETE FROM account WHERE accountname = %s"
                    cursor.execute(delete_query, (username,))
                    connection.commit()
                    print("Your account has been deleted.")
                    break  
                else:
                    print("Account deletion canceled.")
                    time.sleep(2)
            elif log_choice ==4:
                print("logged out")
                time.sleep(2)
                startup()

          
                
            else:
                print("invalid choise try again but pick a number between 1-4")
                time.sleep(2)
        
    else:
        print("Login failed")
        time.sleep(2)
        startup()


def startup():
    print("""----------------Best Bank----------------
          
          
--------please select what you want to do--------
1: signup
2: login
3: exit    
-------------------------------------------------------
        """)
    start_choise = int(input("make your choise "))
    if start_choise == 1:
        signup()
    elif start_choise == 2:
        login()

    elif start_choise == 3:
        print("goodbye")
        exit()
    else:
        print ("that is invalid please try again")
        startup()



startup()
connection.commit()
cursor.close()
connection.close()
