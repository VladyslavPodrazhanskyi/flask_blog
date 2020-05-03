from base1 import db, Puppy

tob = Puppy('Tobik', 11)

db.session.add(tob)
db.session.commit()

print(tob.id)

