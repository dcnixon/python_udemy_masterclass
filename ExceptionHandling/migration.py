import ducks

flock = ducks.Flock()
donald = ducks.Duck()
daisy = ducks.Duck()
huey = ducks.Duck()
dewey = ducks.Duck()
lewis = ducks.Duck()
scrooge = ducks.Duck()
darkwing = ducks.Mallard()
percy = ducks.Penguin()

flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(huey)
flock.add_duck(dewey)
flock.add_duck(lewis)
flock.add_duck(percy)
flock.add_duck(scrooge)
flock.add_duck(darkwing)

flock.migrate()