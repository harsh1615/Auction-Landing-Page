from basic import db, Puppy

#create a new column#
my_puppy = Puppy('rufus',5)
db.session.add(my_puppy)
db.session.commit()