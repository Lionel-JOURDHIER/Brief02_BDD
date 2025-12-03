import pandas as pd
from app.modules.insertion_game import insert_game_1, insert_game_2, insert_game_3
from app.modules.insertion_player import insert_player_1, insert_player_2, insert_player_3, insert_player_4, insert_player_5
from app.modules.insertion_reviews import reviews_to_add
from app.modules.session import create_session

DF_PLAYERS = pd.read_csv("data/players_db.csv")
DF_GAMES = pd.read_csv("data/games_db.csv")
DF_REVIEWS = pd.read_csv("data/reviews_db.csv")

def insert_all_data(df_players:pd.DataFrame = DF_PLAYERS, df_games:pd.DataFrame =  DF_GAMES, df_reviews:pd.DataFrame = DF_REVIEWS):
    
    insert_game_1(df_games)
    insert_game_2(df_games)
    insert_game_3(df_games)
    insert_player_1(df_players)
    insert_player_2(df_players)
    insert_player_3(df_players)
    insert_player_4(df_players)
    insert_player_5(df_players)
    reviews_to_add(df_reviews)

