from print_line import print_line
from private import private
db = {
    "name": "Rakib",
    "phone": 123,
    "password": "123",
    "balance": 10000000
}
send_money_db=[];
cashout_db=[];
payment_db=[];
def my_account():
    def account_details():
        check = private(db.get("password"))
        if (check):
            print_line(f"\nMy Name is {db.get('name')}.")
            print_line(f"My phone Number is {db.get('phone')}.")
            print_line(f"My available balance is {db.get('balance')}.\n")
        else:
            print_line("\nAuthorize errors\n")

    def db_function():
        return db
    return [account_details, db_function,send_money_db,cashout_db,payment_db]
