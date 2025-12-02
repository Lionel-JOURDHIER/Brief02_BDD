import pandas as pd

from app.db.tables import Reviews
from app.modules.get_reviews import existing_review
from app.modules.session import create_session

def reviews_to_add(data: pd.DataFrame):
    """
    Build a list of new Reviews objects or update existing ones.

    Args:
        data: DataFrame with columns 'games', 'players', 'reviews'

    Returns:
        list[Reviews]: new Reviews objects to add to the database
    """
    reviews_to_add = []
    existing_reviews = existing_review()
    session = create_session()
    for row in data.itertuples():
        if pd.isna(row.games) or pd.isna(row.players) or pd.isna(row.reviews):
            continue
        game_id = row.games
        player_id = row.players
        review_score = row.reviews
        review_tuple = (player_id, game_id)
        if review_tuple in existing_reviews :
            review_id = existing_reviews[review_tuple]
            review = session.query(Reviews).filter(Reviews.id == review_id).one()
            review.review_score = review_score
        else : 
            review = Reviews(game_id=game_id, player_id=player_id, review_score=review_score)
            reviews_to_add.append(review)

        for i in reviews_to_add:
            session.add(i)
            
        session.commit()
        session.close()