import pandas as pd

from app.db.tables import City_pc_corresps, Postal_codes, Cities, Countries, Street_types, Players, Addresses, Contacts
from app.modules.session import create_session

def existing_city_cp():
    """
    Retrieve all (city,postal_code) tupple currently stored in the database.

    Returns:
        dict[tuple[int,int], int]: A dictionary mapping city/cp id tupple to its database ID.
    """
    session = create_session()
    existing_city_cps = {(0,0):1}
    try :
        existing_city_cps = {
                (p.postal_code_id, p.city_id) : p.id 
                for p in session.query(City_pc_corresps).all()
            }
        return existing_city_cps
    finally : 
        session.close()

def get_pc_id(name):
    """
    Retrieve the ID of a postal code by its name from the database.
    
    If the postal_code does not exist, it creates a new Genres entry
    and returns its ID.

    Args:
        name (str): The value of the postal_code.

    Returns:
        int: The ID of the postal_code if found, otherwise None.
    """
    session = create_session()
    try :
        Postal_code_id = session.query(Postal_codes.id).filter(Postal_codes.postal_code_value == int(name)).first()
        if Postal_code_id[0] is not None:
            return Postal_code_id[0]
        Postal_code = Postal_codes(postal_code_value = name)
        session.add(Postal_code)
        session.commit()
        return Postal_code.id
    finally : 
        session.close()

def get_city_id(name):
    """
    Retrieve the ID of a city by its name from the database.
    
    If the city does not exist, it creates a new Genres entry
    and returns its ID.

    Args:
        name (str): The name of the city.

    Returns:
        int: The ID of the city if found, otherwise None.
    """
    session = create_session()
    try :
        city_id = session.query(Cities.id).filter(Cities.city_name == name).scalar()
        if city_id is not None:
            return city_id
        City = Cities(city_name = name)
        session.add(City)
        session.commit()
        return City.id
    finally : 
        session.close()    

def existing_city():
    """
    Retrieve cities currently stored in the database.

    Returns:
        dict[str, int]: A dictionary mapping city id tupple to its database ID.
    """
    session = create_session()
    existing_cities = {(0,0):1}
    try :
        existing_cities = {
                 p.city_name : p.id 
                for p in session.query(Cities).all()
            }
        return existing_cities
    finally : 
        session.close()

def existing_country():
    """
    Retrieve countries currently stored in the database.

    Returns:
        dict[str, int]: A dictionary mapping country id tupple to its database ID.
    """
    session = create_session()
    existing_countries = {(0,0):1}
    try :
        existing_countries = {
                 p.country_name : p.id 
                for p in session.query(Countries).all()
            }
        return existing_countries
    finally : 
        session.close()

def existing_street_type():
    """
    Retrieve all street_name currently stored in the database.

    Returns:
        dict[str, int]: A dictionary mapping street_name id tupple to its database ID.
    """
    session = create_session()
    existing_street_types = {(0,0):1}
    try :
        existing_street_types = {
                 p.street_type_name : p.id 
                for p in session.query(Street_types).all()
            }
        return existing_street_types
    finally : 
        session.close()

def existing_postal_code():
    """
    Retrieve all postal codes currently stored in the database.

    Returns:
        dict[int, int]: A dictionary mapping postal codes id tupple to its database ID.
    """
    session = create_session()
    existing_postal_codes = {(0,0):1}
    try :
        existing_postal_codes = {
                 int(p.postal_code_value) : p.id 
                for p in session.query(Postal_codes).all()
            }
        return existing_postal_codes
    finally : 
        session.close()

def existing_player():
    """
    Retrieve all players currently stored in the database.

    Returns:
        dict[tuple(str,str), int]: A dictionary mapping player_name to its database ID.
    """
    session = create_session()
    existing_players = {(0,0):1}
    try :
        existing_players = {
                 (p.first_name, p.last_name) : p.id 
                for p in session.query(Players).all()
            }
        return existing_players
    finally : 
        session.close()