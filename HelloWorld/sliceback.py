letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1]
print(backwards)

# create a string to produce the letter qpo
print(letters[16:13:-1])    # qpo

# slice the string to edcba
print(letters[4::-1])       # edcba

# slice the string to produce the last 8 characters, in reverse order
print(letters[:-9:-1])      # last 8 reversed

print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])