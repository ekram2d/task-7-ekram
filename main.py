from command import command
from user_choice import user_choice
from helpline import helpline
from my_account import my_account
from paybill import pay_bill
from send_money_airtime import send_money
from payment import payment
from cashout import cashout
def main():
    isQuit = False
    [account_details, db,send_money_db,cashout_db,payment_db] = my_account()
    while (not isQuit):
        command()
        choice = user_choice()
        if (choice == 1):
            send_money(db(),send_money_db)
        elif (choice == 2):
            payment(db(),payment_db)
        elif (choice == 3):
            cashout(db(),cashout_db)
        elif (choice == 4):
            pay_bill(db())
        elif (choice == 5):
            account_details()
        elif (choice == 6):
            helpline()
        elif (choice == 7):
            isQuit = True


main()
