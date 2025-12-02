import pandas as pd

from app.db.tables import Reviews
from app.modules.session import create_session

def existing_review():
    """
    Retrieve all (game, player) tupple currently stored in the database.

    Returns:
        dict[tuple[int,int], int]: A dictionary mapping reviews id tupple to its database ID.
    """
    session = create_session()
    existing_reviews = {(0,0):1}
    try :
        existing_reviews = {
                (p.player_id, p.game_id) : p.id 
                for p in session.query(Reviews).all()
            }
        return existing_reviews
    finally : 
        session.close()