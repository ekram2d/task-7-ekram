def cashout(db: dict, cashout_db: list):
    amount = int(input('\nPlease enter the amount to cash out: \n'))
    if amount > db['balance']:
        print("\nInsufficient balance!\n")
    else:
        mobile = input("\nPlease enter mobile number: ")
        cashout_db.append({mobile: amount})
        print("\nCashout money list:")
        for transaction in cashout_db:
            for recipient, money_sent in transaction.items():
                print(f"Recipient: {recipient}, Amount: {money_sent}")
        db.update({"balance": db["balance"] - amount})
