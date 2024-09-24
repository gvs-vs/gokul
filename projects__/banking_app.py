class Account:

    
    def __init__(self,account_number,owner,balance=0):
        self.account_number = account_number
        self.owner= owner
        self.balance=balance

    #defining method to deposit money
    def deposit(self,amount):

        if amount >0:
            self.balance += amount
            print(f"Deposited successfully! New balance: {self.balance}")
        else:
            print("Enter a valid amount to deposit")

    #defining method to withdraw

    def withdraw(self,amount):

        if 0< amount <= self.balance:
            self.balance -= amount
            print(f"Withdrwal is succesfull! New balance : {self.balance}")

        else:

            print("Insufficient balance")

    #define method for balance:

    def balance(self):

        print(f"Account balance: {self.balance}")

    
#creating main function for user interference

def main():

    account ={}

    #creating function to create account

    def create_account():
            account_number= input("Enter a new account number:  ")

            if account_number in account:

                print("Account already exits!")
            
            else:
                owner= input("Enter account owner name: ")
                account[account_number] = Account(account_number,owner)

                print(f"Account created succesfully for {owner}!")
        
        #creating function to access account

    def access_account():
            account_number= input("Enter your account number: ")

            if account_number in account:
                account= account[account_number]
                print(f"Welcome, {account_number}! ")
                

                # Now defining user interaction menu

                while True:
                    print("1. Check balance ")
                    print("2.Deposit Money")
                    print("3. Withdraw money")
                    print("4. Exit")

                    choice= input("Choose an option: ")

                    if choice== '1':
                        account.check_balance()

                    elif choice == '2':
                        amount = float(input("Enter the amount to deposit: "))
                        account.deposit(amount)

                    
                    elif choice == '3':
                        amount = float(input("Enter the withdrawal amount: "))
                        account.withdrawal(amount)

                    elif choice == '4':
                        print("Logging out....")
                        break
                    
                    else:

                        print("Invalid option ")

                
                while True:

                    print("n-- Welcome to Bank---")

                    print("1. Create a new account")

                    print("2. Access existing account")

                    print("3. Exit")

                    choice =  input("Choose an option: ")

                    if choice == '1':
                        create_account()

                    elif choice == '2':
                        access_account()

                    elif choice == '3':
                        print("Thank you for using Bank! ")
                        break

                    else:
                        print("Invalid option...")


if __name__ == "__main__":

 main()




        

            






    
        