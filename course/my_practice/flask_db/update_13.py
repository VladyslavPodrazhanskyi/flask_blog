from base import db, Puppy

puppy_thirteen = Puppy.query.get(13)
puppy_thirteen.name = 'Tarzan'
db.session.add(puppy_thirteen)
db.session.commit()