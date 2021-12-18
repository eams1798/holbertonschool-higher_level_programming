#!/usr/bin/python3
"""Start link class to table in database
"""


if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    connection = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                             sys.argv[2],
                                                             sys.argv[3])
    engine = create_engine(connection, pool_pre_ping=True)

    AllSessions = sessionmaker(bind=engine)
    session = AllSessions()

    Base.metadata.create_all(engine)

    for state in session.query(State).filter(State.name.like('%a%')):
        session.delete(state)

    session.commit()

    session.close()
