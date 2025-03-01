print("WELCOME TO StarBank")  
user_id = 5678 
security_pin = 4321 
account_balance = 1000000 

entered_id = int(input("Enter your Login ID: ")) 

if entered_id == user_id: 
    print("LOGIN SUCCESSFUL") 
    print("Welcome, MR. ANDERSON") 
    print("Your current balance is:", account_balance) 
    
    
    withdrawal_amount = int(input("Enter the amount you want to withdraw: ")) 
    
    if withdrawal_amount <= account_balance: 
        entered_tpin = int(input("To proceed with your withdrawal, enter the transaction PIN: ")) 
        
        if entered_tpin == security_pin: 
            account_balance -= withdrawal_amount  # Deduct the amount from the account balance
            print("Transaction Successful!") 
            print("Your remaining balance is:", account_balance) 
        else:  
            print("INVALID TRANSACTION PIN") 
    else: 
        print("INSUFFICIENT BALANCE") 
else: 
    print("INVALID LOGIN ID")
