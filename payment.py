def payment(db: dict, payment_db: list):
    amount = int(input('\nPlease enter the amount to send: \n'))
    if amount > db['balance']:
        print("\nInsufficient balance!\n")
    else:
        mobile = input("\nPlease enter mobile number: ")
        payment_db.append({mobile: amount})
        print("\nPayment money list:")
        for payment_info in payment_db:
            for mobile, money in payment_info.items():
                print(f"Mobile = {mobile}  Money = {money}")
        db.update({"balance": db["balance"] - amount})

