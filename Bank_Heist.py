class NegativeAmountError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

def transfer_money(accounts, sender, receiver, amount):
    try:
        amount = float(amount)
        
        if amount < 0:
            raise NegativeAmountError("ERROR: Cannot transfer a negative amount!")

        if sender not in accounts or receiver not in accounts:
            raise KeyError("ERROR: One of the accounts does not exist!")

        if accounts[sender] < amount:
            raise InsufficientFundsError("ERROR: Insufficient funds for this transaction!")

        accounts[sender] -= amount
        accounts[receiver] += amount
        print(f"Transaction Successful: {sender} → {receiver} | Amount: ${amount:.2f}")

    except ValueError:
        print("ERROR: Invalid input! Please enter a numeric amount.")
    except NegativeAmountError as e:
        print(e)
    except InsufficientFundsError as e:
        print(e)
    except KeyError as e:
        print(e)


accounts = {
    "Thief1": 5000.00,
    "Thief2": 3000.00,
    "Hacker": 10000.00
}

transfer_money(accounts, "Thief1", "Thief2", 2000) 
transfer_money(accounts, "Thief1", "Thief2", 6000)  
