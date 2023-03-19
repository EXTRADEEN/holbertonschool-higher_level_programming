#!/usr/bin/python3
""" script that print all City objects from the database
"""

import sys
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
                           
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State)\
            .filter(City.state_id == State.id)\
            .order_by(City.id):
        
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
