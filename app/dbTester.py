import database_handler
from database_handler import db_functions
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker
from random import randint

engine = create_engine('mysql+pymysql://sqlusr:Raspberry@LARRY/PieFace')

connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()



db = db_functions()

name = "MediaSet" + str(randint(1, 100))
mtype = 0
content = [{"/home/pieface/goose.mp4", "/home/pieface/goose.mp4"}]
resolution = "1920x1080"
pause = randint(1, 1000)
active = 0
default = 0
storage = "/home/goose/potato.mp4"





#db.get_all_media_sets(session)
db.insert_media_set(session, name, type, resolution, content, pause, active, default, storage)

connection.close()

