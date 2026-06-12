#!/usr/bin/python3
"""Delete all State objects containing the letter a using SQLAlchemy."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    session = Session(engine)

    states = session.query(State).filter(State.name.contains("a")).all()

    for state in states:
        session.delete(state)

    session.commit()
    session.close()
