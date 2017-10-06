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


class main():
        def run(self, session):
            

            '''
            #   INSERT
            if not session.query(exists().where(MediaSets.Name == 'MediaSetPotato')).scalar():
                med_set = MediaSets()
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

            #   test, jestli v DB dany zaznam existuje:
            #print session.query(Address).filter_by(city='City WTF').count()
            #print bool( session.query(Address).filter_by(city='City WTF').count() )

'''



            #   SELECT
            if session.query(exists().where(MediaSets.IsActive == 0)).scalar():
                a2 = session.query(MediaSets).filter_by(IsActive=0)
                for set in a2:
                    print "ID: " + str(set.ID)  + " Name: " + set.Name + " Res: " + set.Resolution
                #print a2[0].ID


'''
            #   UPDATE
            if session.query(exists().where(User.email == 'test@example.net')).scalar():
                session.query(User).filter_by(email='test@example.net').update({"nick": "a"})
                session.commit()

            if session.query(exists().where(User.email == 'test@example.net')).scalar():
                u = session.query(User).filter_by(email='test@example.net').first()
                u.nick = "b"
                session.commit()


            #   DELETE
            if session.query(exists().where(User.email == 'test@example.net')).scalar():
                session.query(User).filter_by(email='test@example.net').delete()
                session.commit()

            if session.query(exists().where(Address.city == 'City WTF')).scalar():
                session.query(Address).filter_by(city='City WTF').delete()
                session.commit()

'''


