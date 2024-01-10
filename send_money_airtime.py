def send_money(db: dict, send_money_db: list):
    amount = int(input('\nPlease enter the amount to send: \n'))
    if amount > db['balance']:
        print("\nInsufficient balance!\n")
    else:
        mobile = input("\nPlease enter mobile number: ")
        send_money_db.append({mobile: amount})
        print("\nSend money list:")
        for transaction in send_money_db:
            for recipient, money_sent in transaction.items():
                print(f"Recipient: {recipient}, Amount: {money_sent}")
        db.update({"balance": db["balance"] - amount})
