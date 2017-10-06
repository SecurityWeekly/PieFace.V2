import database_handler_sqlalc
from database_handler_sqlalc import main
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('mysql+pymysql://sqlusr:Raspberry@LARRY/PieFace')

connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

main().run(session)

connection.close()
