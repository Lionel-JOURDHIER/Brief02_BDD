import pandas as pd

from app.db.tables import Games, Genres, Platforms, Publishers, Release_years
from app.modules.session import create_session

def get_genre_id(name):
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
    