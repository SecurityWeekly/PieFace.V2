import database_handler
from database_handler import db_functions

from sqlalchemy.orm import relationship, sessionmaker
from random import randint

db = db_functions()



for MediaSet in db.session.query(MediaSets):
     print user

