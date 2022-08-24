# Store time information in the database so that the original time can be reconstructed.
# UTC time must still be stored
#
# Modify rollback program to include an extra column in the database.
# Modify checkdb to retrieve the original time and display it along with the UTC time.


import sqlite3
import datetime
import pytz
import time

db = sqlite3.connect("accountsChal.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history (utctime TIMESTAMP NOT NULL, localtime TIMESTAMP NOT NULL," 
           " account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY (utctime, account))")
# last statement of line above defines composite key
db.execute("CREATE VIEW IF NOT EXISTS localhistory AS "
           "SELECT strftime('%Y-%m-%d %H:%M:%f', history.utctime, 'localtime') AS localtime,"
           "history.account, history.amount FROM history ORDER BY history.utctime")
# To be implemented Audit Code to check if transactions and balance match


class Account(object):

    @staticmethod
    def _current_time():
        utc_time = pytz.utc.localize(datetime.datetime.utcnow())
        local_time = datetime.datetime.now().astimezone()
        return utc_time, local_time

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
        new_balance = self._balance + amount
        deposit_utctime, deposit_localtime = Account._current_time()
        time.sleep(0.000001)
        db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
        db.execute("INSERT INTO history VALUES(?, ?, ?, ?)", (deposit_utctime, deposit_localtime, self.name, amount))
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
    john = Account("John")
    john.deposit(1010)
    john.deposit(10)

    john.withdraw(30)
    john.deposit(10)
    john.withdraw(0)
    john.show_balance()

    terry = Account("TerryJ")
    graham = Account("Graham", 9000)
    eric = Account("Eric", 7000)
    michael = Account("Micheal")
    terryG = Account("TerryG")

    db.close()
