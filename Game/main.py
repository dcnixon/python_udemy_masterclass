from enemy import Enemy, Troll, Vampyre, VampyreKing

# ugly_troll = Troll("Pug")
# print("Ugly troll - {}".format(ugly_troll))
#
# another_troll = Troll("Ug")
# print("Another troll - {}".format(another_troll))
# another_troll.take_damage(10)
# print(another_troll)
#
# brother = Troll("Urg")
# print(brother)
#
# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()
#
# old_vamp = Vampyre("Vlad")
# print(old_vamp)
# old_vamp.take_damage(6)
# print(old_vamp)
#
# print("-" * 40)
# another_troll.take_damage(30)
# print(another_troll)
#
# print("-" * 40)

dracula = VampyreKing("Dracula")
print(dracula)

while dracula._alive:
    dracula.take_damage(3)
    # print(old_vamp)