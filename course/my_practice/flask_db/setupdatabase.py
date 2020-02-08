from base import db, Puppy

# create all the models(tables) of the db
db.create_all()

#create row of the table Puppy:

sam = Puppy('Sammy', 5)
frank = Puppy('Frank', 2)

#Should be None (as rows has not been added yet)
print(sam.id)
print(frank.id)

db.session.add_all([sam, frank]) # added all rows

# add rows one by one
# db.session.add(sam)
# db.session.add(frank)

db.session.commit()

print(sam.id)
print(frank.id)