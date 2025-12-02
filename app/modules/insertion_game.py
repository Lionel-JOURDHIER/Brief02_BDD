import pandas as pd

from app.db.tables import Games, Genres, Platforms, Publishers, Release_years
from app.modules.session import create_session

def publishers_to_add(data: pd.DataFrame):
    data_sorted = data.sort_values(by="Publisher_id")
    publishers_to_add = [Publishers(publisher_name="No publisher")]
    seen_publishers = {"NULL", None, ""}
    #! ADD CHECK PUBLISHERS
    for row in data_sorted.itertuples():
        publisher_name = row.Publisher
        if pd.isna(publisher_name):
            continue
        if publisher_name not in seen_publishers:
            seen_publishers.add(publisher_name)
            publisher_to_add = Publishers(publisher_name=row.Publisher)
            publishers_to_add.append(publisher_to_add)
    return publishers_to_add

def genres_to_add(data: pd.DataFrame):
    data_sorted = data.sort_values(by="Genre_id")
    genres_to_add = [Genres(genre_name="No genre")]
    seen_genres = {"NULL", None, ""}
    #! ADD CHECK GENRES
    for row in data_sorted.itertuples():
        genre_name = row.Genre
        if pd.isna(genre_name):
            continue
        if genre_name not in seen_genres:
            seen_genres.add(genre_name)
            genre_to_add = Genres(genre_name=row.Genre)
            genres_to_add.append(genre_to_add)
    return genres_to_add

def release_years_to_add(data: pd.DataFrame):
    data_sorted = data.sort_values(by="Year_id")
    years_to_add = [Release_years(release_year="No release_year")]
    seen_years = {"NULL", None, ""}
    #! ADD CHECK RELEASE_YEAR
    for row in data_sorted.itertuples():
        year = row.Year
        if pd.isna(year):
            continue
        if year not in seen_years:
            seen_years.add(year)
            year_to_add = Release_years(release_year=int(float(row.Year)))
            years_to_add.append(year_to_add)
    return years_to_add

def platforms_to_add(data: pd.DataFrame):
    data_sorted = data.sort_values(by="Platform_id")
    platforms_to_add = [Platforms(platform_name="No platform")]
    seen_platforms = {"NULL", None, ""}
    #! ADD CHECK PLATFORM
    for row in data_sorted.itertuples():
        platform = row.Platform
        if pd.isna(platform):
            continue
        if platform not in seen_platforms:
            seen_platforms.add(platform)
            platform_to_add = Platforms(platform_name=row.Platform)
            platforms_to_add.append(platform_to_add)
    return platforms_to_add

def games_to_add(data: pd.DataFrame):
    games_to_add = []
    for row in data.itertuples():
        release_year_id = row.Year_id
        if pd.isna(release_year_id):
            release_year_id = 1
        publisher_id = row.Publisher_id
        if pd.isna(publisher_id):
            publisher_id = 1
        platform_id = row.Platform_id
        if pd.isna(platform_id):
            platform_id = 1
        genre_id = row.Genre_id
        if pd.isna(genre_id):
            genre_id = 1
        game_to_add = Games(
            rank_game = row.Rank,
            game_name = row.Name,
            NA_sales = row.NA_Sales,
            EU_sales = row.EU_Sales,
            JP_sales = row.JP_Sales,
            other_sales = row.Other_Sales,
            global_sales = row.Global_Sales,
            release_year_id = release_year_id,
            publisher_id = publisher_id,
            platform_id = platform_id,
            genre_id = genre_id
            )
        games_to_add.append(game_to_add)
    return games_to_add

def games_all_to_db (data: pd.DataFrame):
    
    session = create_session()

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
    session.close()