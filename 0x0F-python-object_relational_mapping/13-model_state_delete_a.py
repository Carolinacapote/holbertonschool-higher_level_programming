#!/usr/bin/python3
'''
Script that deletes all State objects with a name containing the letter
'a' from the database
'''
from model_state import Base, State
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

    states = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id)

    for state in states:
        session.delete(state)

    session.commit()
    session.close()
