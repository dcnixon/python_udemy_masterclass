# jabber = open("C:\\Users\\DanNix\\Downloads\\sample.txt", 'r')
#
# for line in jabber:
#     if "jabberwock" in line.casefold():
#         print(line, end="")
#
# jabber.close()
# with open("sample.txt", "r") as jabber:
#     for line in jabber:
#         if "jab" in line.casefold():
#             print(line, end="")
# with open("sample.txt", "r") as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end="")
#         line = jabber.readline()
#
# with open("sample.txt", "r") as jabber:
#     lines = jabber.readlines()
# print(lines)
# for line in lines:
#     print(line, end="")

with open("sample.txt", "r") as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end="")

with open("sample.txt", "r") as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end="")