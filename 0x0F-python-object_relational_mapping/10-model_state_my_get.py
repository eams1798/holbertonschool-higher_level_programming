#!/usr/bin/python3
"""Start link class to table in database
"""


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    connection = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                             argv[2],
                                                             argv[3])
    engine = create_engine(connection, pool_pre_ping=True)

    AllSessions = sessionmaker(bind=engine)
    session = AllSessions()

    Base.metadata.create_all(engine)

    state = session.query(State).filter(State.name == argv[4]).first()
    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()
