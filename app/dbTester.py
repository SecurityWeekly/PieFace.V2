import database_handler
from database_handler import db_functions, MediaSets

from sqlalchemy.orm import relationship, sessionmaker
from random import randint



mid = 5
name = "MediaSet" + str(randint(1, 100))
mtype = 0
content = 0
resolution = "1920x1080"
pause = randint(1, 1000)
active = 0
default = 0
storage = "/home/goose/potato.mp4"



db = db_functions()

db.insert_media_set()




