#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""
import sys
from model_state import Base, State
from model_city import City
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
    
    cities_with_states = session.query(State, City).filter(
        State.id == City.state_id
    ).order_by(City.id).all()
    
    for state, city in cities_with_states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
        
    session.close()
