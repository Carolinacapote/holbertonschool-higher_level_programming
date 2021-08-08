#!/usr/bin/python3
'''
Script that prints the first State object from the database hbtn_0e_6_usa
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

    statenames_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for i in statenames_with_a:
        print('{}: {}'.format(i.id, i.name))
