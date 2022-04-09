#!/usr/bin/python3
"""Print all state from states where contain letter a"""

from ast import keyword
from queue import Empty
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    s = 'mysql+mysqldb://'
    n = sys.argv[1]
    p = sys.argv[2]
    b = sys.argv[3]
    state = sys.argv[4]
    i = '@localhost'
    engine = create_engine('{}{}:{}{}/{}'.format(s, n, p, i, b))
    Base.metadata.create_all(engine)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter_by(name=sys.argv[4])

    for state in result:
        print("{}".format(state.id))
        i = 1
    if i != 1:
        print("Not found")
