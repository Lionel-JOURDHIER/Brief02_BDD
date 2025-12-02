from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.tables.base import Base


# ENGINE = create_engine("sqlite:///ma_base_clients.db", echo=True)
#! DB test à retirer pour prod
ENGINE = create_engine("sqlite:///clients_test.db", echo=True)


def create_session(engine = ENGINE):
    '''
    Create and return a new SQLAlchemy session.

    Args : 
        engine : sqlalchemy.Engine
            The SQLAlchemy engine connected to the database.

    Returns : 
        Session
            A new SQLAlchemy session instance.
    '''
    try : 
        # create the tables
        Base.metadata.create_all(engine)
        # open the session
        Session = sessionmaker(bind=engine)
        return Session()
    except Exception as e:
        print(f"Error creating database session: {e}")

