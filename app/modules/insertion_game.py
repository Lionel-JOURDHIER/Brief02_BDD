import pandas as pd

from app.db.tables import Games, Genres, Platforms, Publishers, Release_years, GamesPlatforms
from app.modules.session import create_session
from app.modules.get_game import get_game_id, get_genre_id, get_platform_id, get_publisher_id, get_year_id, existing_genre, existing_publisher, existing_year, existing_platform, existing_game

def init_bdd_game():
    """
    Initialize the database with default entries for essential lookup tables.
    """
    try : 
        init_bdd_list = []
        session = create_session()
        if not existing_publisher():
            init_bdd_list.append(Publishers(publisher_name="no publisher"))
        if not existing_genre():
            init_bdd_list.append(Genres(genre_name="no genre"))
        if not existing_year():
            init_bdd_list.append(Release_years(release_year="no release_year"))
        if not existing_platform():
            init_bdd_list.append(Platforms(platform_name="no platform"))
        session.add_all(init_bdd_list)
        session.commit()
    finally:
        session.close()

def publishers_to_add(data: pd.DataFrame):
    """
    Build a list of new Publishers objects to insert into the database.

    This function:
      - Sorts the input DataFrame by "Publisher_id"
      - Loads the list of existing publishers already stored in the database
      - Iterates over each row of the DataFrame
      - Skips invalid or empty publisher names (NaN, None, "", "NULL")
      - Skips publishers already existing in the database
      - Avoids duplicates within the current dataset using a local set
      - Returns a list of Publisher ORM objects ready for insertion

    Args : 
        data : pd.DataFrame
            The DataFrame containing a "Publisher" column and a "Publisher_id" column.

    Returns :
        list[Publishers]
            A list of SQLAlchemy `Publishers` objects that are not yet present
            in the database and should be inserted.
    """
    data_sorted = data.sort_values(by="Publisher_id")
    publishers_to_add = []
    seen_publishers = {"NULL", None, ""}
    # Extract the existing publisher list
    existing_publishers = existing_publisher()
    for row in data_sorted.itertuples():
        publisher_name = row.Publisher

        # Check if Nan
        if pd.isna(publisher_name):
            continue
        
        publisher_name_low = str(publisher_name).strip().lower()

        # Check if in the existing publisher list
        if publisher_name_low in existing_publishers or publisher_name_low in seen_publishers: 
            continue
        seen_publishers.add(publisher_name_low)
        publisher_to_add = Publishers(publisher_name=publisher_name)
        publishers_to_add.append(publisher_to_add)
    return publishers_to_add

def genres_to_add(data: pd.DataFrame):
    """
    Build a list of new Genres objects to insert into the database.
    
    This function:
      - Sorts the input DataFrame by "Genre_id"
      - Loads the list of existing genres already stored in the database
      - Iterates over each row of the DataFrame
      - Skips invalid or empty publisher names (NaN, None, "", "NULL")
      - Skips genres already existing in the database
      - Avoids duplicates within the current dataset using a local set
      - Returns a list of Genres ORM objects ready for insertion

    Args : 
        data : pd.DataFrame
            The DataFrame containing a "Genre" column and a "Genre_id" column.

    Returns :
        list[Genres]
            A list of SQLAlchemy `Genres` objects that are not yet present
            in the database and should be inserted.

    """
    data_sorted = data.sort_values(by="Genre_id")
    genres_to_add = []
    seen_genres = {"NULL", None, ""}
    existing_genres = existing_genre()
    for row in data_sorted.itertuples():
        genre_name = row.Genre
        if pd.isna(genre_name):
            continue
        genre_name_low = str(genre_name).strip().lower()
        if  genre_name_low in existing_genres or genre_name_low in seen_genres:
            continue
        seen_genres.add(genre_name_low)
        genre_to_add = Genres(genre_name=genre_name)
        genres_to_add.append(genre_to_add)
    return genres_to_add

def release_years_to_add(data: pd.DataFrame):
    """
    Build a list of new Release_years objects to insert into the database.
    
    This function:
      - Sorts the input DataFrame by "Year_id"
      - Loads the list of existing year already stored in the database
      - Iterates over each row of the DataFrame
      - Skips invalid or empty publisher names (NaN, None, "", "NULL")
      - Skips release_year already existing in the database
      - Avoids duplicates within the current dataset using a local set
      - Returns a list of Release_years ORM objects ready for insertion

    Args : 
        data : pd.DataFrame
            The DataFrame containing a "Year" column and a "Year_id" column.

    Returns :
        list[Release_years]
            A list of SQLAlchemy `Release_years` objects that are not yet present
            in the database and should be inserted.
    """
    data_sorted = data.sort_values(by="Year_id")
    years_to_add = []
    seen_years = {"NULL", None, ""}
    existing_years = existing_year()
    print(existing_years)
    for row in data_sorted.itertuples():
        year = row.Year
        if pd.isna(year):
            continue
        year_int = int(float(row.Year))
        if year_int in existing_years or year_int in seen_years:
            continue
        seen_years.add(year_int)
        year_to_add = Release_years(release_year=year_int)
        years_to_add.append(year_to_add)
    return years_to_add

def platforms_to_add(data: pd.DataFrame):
    """
    Build a list of new Platforms objects to insert into the database.
    
    This function:
      - Sorts the input DataFrame by "Platform_id"
      - Loads the list of existing platform already stored in the database
      - Iterates over each row of the DataFrame
      - Skips invalid or empty publisher names (NaN, None, "", "NULL")
      - Skips platform already existing in the database
      - Avoids duplicates within the current dataset using a local set
      - Returns a list of Platforms ORM objects ready for insertion

    Args : 
        data : pd.DataFrame
            The DataFrame containing a "Platform" column and a "Platform_id" column.

    Returns :
        list[Platforms]
            A list of SQLAlchemy `Platforms` objects that are not yet present
            in the database and should be inserted.

    """
    data_sorted = data.sort_values(by="Platform_id")
    platforms_to_add = []
    seen_platforms = {"NULL", None, ""}
    existing_platforms = existing_platform()
    for row in data_sorted.itertuples():
        platform = row.Platform
        if pd.isna(platform):
            continue
        platform_low = str(platform).strip().lower()
        if platform_low in existing_platforms or platform_low in seen_platforms:  
            continue
        seen_platforms.add(platform_low)
        platform_to_add = Platforms(platform_name=platform)
        platforms_to_add.append(platform_to_add)
    return platforms_to_add

def games_to_add(data: pd.DataFrame):
    """
    Build a list of new Games objects to insert into the database.
    
    This function:
      - Iterates over each row of the input DataFrame
      - Skips invalid or missing foreign key IDs (NaN) by assigning default values
      - Skips games already existing in the database
      - Avoids duplicates within the current dataset using existing game names
      - Returns a list of Games ORM objects ready for insertion

    Args : 
        data : pd.DataFrame
            The DataFrame containing game information with the following columns:
            "Rank", "Name", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales",
            "Global_Sales", "Year_id", "Publisher_id", "Platform_id", "Genre_id"

    Returns :
        list[Games]
            A list of SQLAlchemy `Games` objects that are not yet present
            in the database and should be inserted.
    """
    games_to_add = []
    seen_games = {"NULL", None, ""}
    existing_games = existing_game()
    existing_publishers = existing_publisher()
    existing_genres = existing_genre()
    existing_years = existing_year()
    for row in data.itertuples():
        
        release_year = row.Year
        if pd.isna(release_year):
            release_year_id = 1
        else : 
            release_year_int = int(float(release_year))
        if release_year_int in existing_years :
            release_year_id = existing_years.get(release_year_int, 1)
        else : 
            release_year_id = get_game_id(release_year_int)

        publisher = row.Publisher
        if pd.isna(publisher):
            publisher_id = 1
        publisher_low = str(publisher).strip().lower()
        if publisher_low in existing_publishers:
            publisher_id = existing_publishers.get(publisher_low, 1)
        else : 
            publisher_id = get_publisher_id(publisher)

        genre = row.Genre
        if pd.isna(genre):
            genre_id = 1
        genre_low = str(genre).strip().lower()
        if genre_low in existing_genres :
            genre_id = existing_genres.get(genre_low,1)
        else : 
            genre_id = get_genre_id(genre)
        
        game_name = row.Name
        game_name_low = str(game_name).strip().lower()

        if game_name_low in existing_games or game_name_low in seen_games: 
            continue
        seen_games.add(str(game_name_low))
        game_to_add = Games(
            game_name = row.Name,
            NA_sales = row.NA_Sales,
            EU_sales = row.EU_Sales,
            JP_sales = row.JP_Sales,
            other_sales = row.Other_Sales,
            global_sales = row.Global_Sales,
            release_year_id = release_year_id,
            publisher_id = publisher_id,
            genre_id = genre_id
            )
        games_to_add.append(game_to_add)
    return games_to_add

def games_all_to_db (data: pd.DataFrame):
    """
    Insert all games-related data into the database in the correct order.

    This function:
      - Opens a database session
      - Adds publishers, genres, release years, and platforms to the database first
      - Adds games after the related foreign key objects have been inserted
      - Commits the transaction and closes the session
      - Ensures the session is closed even if an error occurs

    Args:
        data : pd.DataFrame
            The DataFrame containing all game information, including columns for:
            "Publisher", "Genre", "Year", "Platform", "Name", "Rank", 
            "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"

    Returns:
        None
    """
    session = create_session()
    try: 
        for i in publishers_to_add(data):
            session.add(i)

        for i in genres_to_add(data):
            session.add(i)

        for i in release_years_to_add(data):
            session.add(i)
            
        for i in platforms_to_add(data):
            session.add(i)

        for i in games_to_add(data):
            session.add(i)
            
        session.commit()
    finally:
        session.close()
