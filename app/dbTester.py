import database_handler
from database_handler import db_functions

from sqlalchemy.orm import relationship, sessionmaker
from random import randint

db = db_functions()
connection = db.engine.connect()
Session = sessionmaker(bind=db.engine)
session = Session()




mid = 1
name = "MediaSet" + str(randint(1, 100))
mtype = 0
content = 0
resolution = "1920x1080"
pause = randint(1, 1000)
active = 0
default = 0
storage = "/home/goose/potato.mp4"





#db.get_all_media_sets(session)
#db.insert_media_set(session, name, mtype, resolution, content, pause, active, default, storage)
#db.update_media_set_by_id(session, mid, name, mtype, resolution, content, pause, active, default, storage)

print(db.get_media_set_by_id(session, mid))


connection.close()

