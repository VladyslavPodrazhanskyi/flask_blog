from pprint import pprint
from models2 import db, Puppy, Toy, Owner


kate = Puppy('Kate')
richard = Puppy('Richard')

db.session.add_all([kate, richard])
db.session.commit()

first_pup = Puppy.query.get(5)
second_pup = Puppy.query.get(6)

pprint(first_pup)
pprint(second_pup)

first_pup.report_toys()

semen = Owner('Semen', 6)

ball1 = Toy('ball', 6)
rabbit_paw1 = Toy('rabbit_paw', 6)



db.session.add_all([semen, ball1, rabbit_paw1])
db.session.commit()

first_pup = Puppy.query.get(6)
second_pup = Puppy.query.get(7)


pprint(first_pup)
pprint(second_pup)

print(type(first_pup))
first_pup.report_toys()



