from sqlalchemy import create_engine, exists
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, LargeBinary, DateTime


Base = declarative_base()


class MediaSets(Base):
    __tablename__ = 'MediaSets'
    ID = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False)
    Type = Column(Integer, nullable=False, unique=True)
    Resolution = Column(String, nullable=False)
    Content = Column(LargeBinary, nullable=False)
    DateCreated = Column(DateTime, nullable=False)
    PauseTime = Column(Integer, nullable=False)
    IsActive = Column(Integer, nullable=False)
    IsDefault = Column(Integer, nullable=False)
    StorageLocation = Column(String, nullable=False)

class db_functions():
        
    
    def insert_media_set(self, session, name, type, resolution, content, pause, active, default, storage):
        med_set = MediaSets()
        # check to see if media set allready exists
        if not session.query(exists().where(MediaSets.Name == 'MediaSetPotato6')).scalar():
            med_set.ID = 0
            med_set.Name = "MediaSetPotato"
            med_set.Type = 1
            med_set.Resolution = "1024x720"
            med_set.Content = "Column(Blob, nullable=False)"
            med_set.DateCreated = datetime.now()
            med_set.PauseTime = 698
            med_set.IsActive = 0
            med_set.IsDefault = 0
            med_set.StorageLocation = "/yourmom.mpg"

                    
            session.add(med_set)
            session.commit()
        else:
            print("That media set allready exists!") 

    def get_all_media_sets(self, session):
        
        #to get first row use .first()
        Sets = session.query(MediaSets)
        for set in Sets:
            print "ID: " + str(set.ID)  + " Name: " + set.Name + " Res: " + set.Resolution


    def update_media_set_name(self, session):
        if session.query(exists().where(MediaSets.Name == 'MediaSetPotato')).scalar():
            sets = session.query(MediaSets).filter_by(Name='MediaSetPotato').first()
            sets.Name = "MediaSetPotatoUpdate"
            session.commit()


    def delete_media_set(self, session):
        if session.query(exists().where(MediaSets.Name == 'MediaSetPotato')).scalar():
            session.query(MediaSets).filter_by(Name='MediaSetPotato').delete()
            session.commit()
        
