#!/usr/bin/python3
"""Print all state from states"""

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    s = 'mysql+mysqldb://'
    n = sys.argv[1]
    p = sys.argv[2]
    b = sys.argv[3]
    i = '@localhost'
    engine = create_engine('{}{}:{}{}/{}'.format(s, n, p, i, b))
    Base.metadata.create_all(engine)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    rcity = session.query(City).all()
    rstate = session.query(State).all()

    for city in rcity:
        for state in rstate:
            if (state.id == city.state_id):
                print("{}: ({}) {}".format(state.name, city.id, city.name))
