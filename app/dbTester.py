import database_handler
from database_handler import db_functions
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('mysql+pymysql://sqlusr:Raspberry@LARRY/PieFace')

connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()



db = db_functions()


db.get_all_media_sets(session)

connection.close()
