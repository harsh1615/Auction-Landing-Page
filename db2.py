from basic importdb,Puppy

###create all the tables model
db.create_all()

frank = Puppy('frankie',4)
sam = puppy('sammy',3)

#none
#none
print(sam.id)
print(frank.id)

db.session.ass_all([sam,frank])
db.session.commit()

peint(sam.id)
print(frank.id)