vowels = frozenset("aeiou")

letters = set(input("Please enter your text: ").casefold())
# Return the letters as a list

# for letter in letters
#     if letter.isalpha() and letter.casefold() in vowels
print(sorted(letters.difference(vowels)))
# for letter in text:
#     letters += letter
# print(letters)
