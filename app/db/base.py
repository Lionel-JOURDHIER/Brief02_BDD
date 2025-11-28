from sqlalchemy.orm import declarative_base

# Here we create a variable that holds the methods from declarative_base
# All table classes will inherit from this base.
Base = declarative_base()