#!/usr/bin/python3
'''
Script that prints all City objects from the database hbtn_0e_14_usa
'''
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    user_name = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user_name, passwd, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State, City).filter(State.id == City.state_id).all()

    for city in cities:
        print("{}: ({}) {}".
              format(city.State.name, city.City.id, city.City.name))

    session.close()
