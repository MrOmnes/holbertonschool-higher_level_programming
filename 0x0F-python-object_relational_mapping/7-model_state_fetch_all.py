#!/usr/bin/python3
"""Print all state from states"""

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy import (create_engine)

s = 'mysql+mysqldb://'
n = sys.argv[1]
p = sys.argv[2]
b = sys.argv[3]
i = '@localhost'

if __name__ == "__main__":
    engine = create_engine('{}{}:{}{}/{}'.format(s, n, p, i, b))
    Base.metadata.create_all(engine)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).all()

    for state in result:
        print("{}: {}".format(state.id, state.name))
