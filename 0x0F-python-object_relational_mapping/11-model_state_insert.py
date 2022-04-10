#!/usr/bin/python3
"""Insert States"""

import sys
from model_state import Base, State
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
    newStates = State(name='Louisiana')
    session.add(newStates)
    session.commit()

    print(newStates.id)
