import sqlite3
import datetime
import pytz
import time

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL,"
           " account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY (time, account))")     # defines composite key
db.execute("CREATE VIEW IF NOT EXISTS localhistory AS "
           "SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
           "history.account, history.amount FROM history ORDER BY history.time")
# To be implemented Audit Code to check if transactions and balance match


class Account(object):

    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())
        # local_time = pytz.utc.localize(datetime.datetime.utcnow())
        # return local_time.astimezone()

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print("Retrieved record for {}. ".format(self.name), end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print("Account created for {}. ".format(self.name), end='')
        self.show_balance()

    # TODO Deposit and Withdraw Methods need to create an entry in the history table
    #  Deposit and Withdraw Method need to update the balance in the accounts table
    #  Ensure all the updates are made otherwise roll back all the updates
    def _save_update(self, amount):
        time.sleep(0.000001)
        new_balance = self._balance + amount
        deposit_time = Account._current_time()

        try:
            db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
        except sqlite3.Error:
            db.rollback()
        else:
            db.commit()
            self._balance = new_balance


    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            self._save_update(amount)
            # new_balance = self._balance + amount
            # time.sleep(0.000001)
            # deposit_time = pytz.utc.localize(datetime.datetime.utcnow())
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
            # db.commit()
            # self._balance = new_balance
            print("$ {:.2f} deposited".format(amount / 100))
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._save_update(-amount)
            # new balance = self._balance - amount
            # time.sleep(0.000001)
            # withdrawal_time = pytz.utc.localize(datetime.datetime.utcnow())
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (withdrawal_time, self.name, amount))
            # db.commit()
            # self._balance = new_balance
            print("$ {:.2f} withdrawn".format(amount / 100))
            return amount / 100
        else:
            print("The amount must be greater than zero and no more than your account balance")
            return 0.0

    def show_balance(self):
        print("Balance on account {} is $ {:.2f}".format(self.name, self._balance / 100))



if __name__ == "__main__":
    # Rollback is required because the DB accepts the UPDATE to the account balance only the INSERT statement fails
    # Only the last transaction shows in the DB because each update is overwritten


    john = Account("John")
    john.deposit(1010)          # update (1000 + 1010) insert succeeded > commit > self._balance = new_balance (2010)
    john.deposit(10)            # update (2010 + 10), insert failed > pass self._balance @ 2010 DB @ 2020 - uncommitted
    john.deposit(10)            # update (2010 + 10), insert failed > pass self._balance @ 2010 DB @ 2020 - uncommitted

    john.withdraw(30)           # update (2010 - 30), insert failed > pass self._balance @ 2010 DB @ 1980 - uncommitted
    john.withdraw(0)            # print("The amount must be greater than zero and no more than your account balance")
    john.show_balance()         # Shows balance of 2010

    terry = Account("TerryJ")   # Error only occurs when an account is added after the failed transaction because,
    # the transaction was sent to the DB and gets committed to the DB when the new account is inserted,
    # and the commit for the account is called
    # All the pending updates still occur, but only the last is seen since they all overwrite each other.
    graham = Account("Graham", 9000)
    eric = Account("Eric", 7000)
    michael = Account("Micheal")
    terryG = Account("TerryG")

    db.close()
