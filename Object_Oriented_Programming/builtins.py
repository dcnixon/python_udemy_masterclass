class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 0.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)
print(hamilton.price)

print("Switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)

print("Switch kenwood to gas")
kenwood.power_source = "gas"
print(hamilton.power_source)
print(kenwood.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print((hamilton.__dict__))