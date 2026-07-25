#!/usr/bin/python3
"""Changes the name of a State object from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, dbname
        ), pool_pre_ping=True
    )
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    state_to_update = session.query(State).filter(State.id == 2).first()
    
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
        
    session.close()
