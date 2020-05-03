from base1 import db, Puppy

# Create all the tables (Model ---> Db Tables
db.create_all()

sam = Puppy('Sammy', 5)
bob = Puppy('Bob', 4)
tob = Puppy('Tobik', 11)

print(sam.id)
print(bob.id)

db.session.add_all([sam, bob, tob])
db.session.commit()

print(sam.id)
print(bob.id)
