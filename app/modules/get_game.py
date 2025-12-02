import pandas as pd

from app.db.tables import Games, Genres, Platforms, Publishers, Release_years
from app.modules.session import create_session

def get_genre_id(name):
    """
    Retrieve the ID of a genre by its name from the database.
    
    Prints an error message if the genre does not exist.

    Args:
        name (str): The name of the genre.

    Returns:
        int or None: The ID of the genre if found, otherwise None.
    """
    session = create_session()
    try :
        genre_id = session.query(Genres.id).filter(Genres.genre_name == name).scalar()
        if genre_id is None:
            print("-"*70)
            print(f"No genre found for : '{name}'")
            print("-"*70)
        return genre_id
    finally : 
        session.close()

def get_publisher_id(name):
    """
    Retrieve the ID of a publisher by its name from the database.
    
    Prints an error message if the publisher does not exist.

    Args:
        name (str): The name of the publisher.

    Returns:
        int or None: The ID of the publisher if found, otherwise None.
    """
    session = create_session()
    try :
        publisher_id = session.query(Publishers.id).filter(Publishers.publisher_name == name).scalar()
        if publisher_id is None:
            print("-"*70)
            print(f"No publisher found for : '{name}'")
            print("-"*70)
        return publisher_id
    finally : 
        session.close()


def get_platform_id(name):
    """
    Retrieve the ID of a platform by its name from the database.
    
    Prints an error message if the platform does not exist.

    Args:
        name (str): The name of the platform.

    Returns:
        int or None: The ID of the platform if found, otherwise None.
    """
    session = create_session()
    try :
        platform_id = session.query(Platforms.id).filter(Platforms.platform_name == name).scalar()
        if platform_id is None:
            print("-"*70)
            print(f"No platform found for : '{name}'")
            print("-"*70)
        return platform_id
    finally : 
        session.close()

def get_year_id(name):
    """
    Retrieve the ID of a release_year by its value from the database.
    
    Prints an error message if the release_year does not exist.

    Args:
        name (str): The name of the release_year.

    Returns:
        int or None: The ID of the release_year if found, otherwise None.
    """
    session = create_session()
    try :
        release_year_id = session.query(Release_years.id).filter(Release_years.release_year == name).scalar()
        if release_year_id is None:
            print("-"*70)
            print(f"No release year found for : '{name}'")
            print("-"*70)
        return release_year_id
    finally : 
        session.close()

def get_game_id(name):
    """
    Retrieve the ID of a game by its value from the database.
    
    Prints an error message if the game does not exist.

    Args:
        name (str): The name of the game.

    Returns:
        int or None: The ID of the game if found, otherwise None.
    """    
    session = create_session()
    try :
        game_id = session.query(Games.id).filter(Games.game_name == name).scalar()
        if game_id is None:
            print("-"*70)
            print(f"No game found for : '{name}'")
            print("-"*70)
        return game_id
    finally : 
        session.close()
    
def existing_genre():
    """
    Retrieve all genre names currently stored in the database.

    Returns:
        set[str]: A set containing all existing genre names.
    """
    session = create_session()
    try :
        existing_genres = {
                p[0] for p in session.query(Genres.genre_name).all()
            }
        return existing_genres
    finally : 
        session.close()

def existing_publisher():
    """
    Retrieve all publisher names currently stored in the database.

    Returns:
        set[str]: A set containing all existing publisher names.
    """
    session = create_session()
    try :
        existing_publishers = {
                p[0] for p in session.query(Publishers.publisher_name).all()
            }
        return existing_publishers
    finally : 
        session.close()

def existing_year():
    """
    Retrieve all release_year value currently stored in the database.

    Returns:
        set[str]: A set containing all existing release_year value.
    """
    session = create_session()
    try :
        existing_years = {
                p[0] for p in session.query(Release_years.release_year).all()
            }
        return existing_years
    finally : 
        session.close()
    
def existing_platform():
    """
    Retrieve all platform names currently stored in the database.

    Returns:
        set[str]: A set containing all existing platform names.
    """
    session = create_session()
    try :
        existing_platforms = {
                p[0] for p in session.query(Platforms.platform_name).all()
            }
        return existing_platforms
    finally : 
        session.close()
    
def existing_game():
    """
    Retrieve all game names currently stored in the database.

    Returns:
        set[str]: A set containing all existing game names.
    """
    session = create_session()
    try :
        existing_games = {
                p[0] for p in session.query(Games.game_name).all()
            }
        return existing_games
    finally : 
        session.close()