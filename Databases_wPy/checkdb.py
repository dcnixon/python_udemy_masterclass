import sqlite3

# edit to ask the user for a name and use a WHERE clause to retrieve just the row for that one person
conn = sqlite3.connect("contacts.sqlite")

name = input("Please enter the contact's name: ")

for row in conn.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):
    print(row)

conn.close()
