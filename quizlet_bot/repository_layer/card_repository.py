from typing import List

from sqlalchemy.exc import SQLAlchemyError
from controller import get_db
from entity_layer.card import Card


class CardRepository:
    def __init__(self):
        self.db = next(get_db())

    def user_has_cards(self, user_id: str) -> bool:
        return self.db.query(Card).filter(Card.user_id == user_id).count() > 0

    def get_user_cards(self, user_id: str) -> List[Card]:
        try:
            return self.db.query(Card).filter(Card.user_id == user_id).all()
        except SQLAlchemyError as e:
            print(f"Database error: {e}")
            return []
        finally:
            self.db.close()

    def get_next_unstudied_card(self, user_id: str):
        try:
            return (
                self.db.query(Card).filter_by(user_id=user_id, is_studied=False).first()
            )
        except SQLAlchemyError as e:
            print(f"Database error: {e}")
            return None
        finally:
            self.db.close()

    def reset_studied_cards(self, user_id: int) -> int:
        try:
            updated_rows = (
                self.db.query(Card)
                .filter_by(user_id=user_id, is_studied=True)
                .update({"is_studied": False}, synchronize_session="fetch")
            )
            self.db.commit()
            return updated_rows
        except SQLAlchemyError as e:
            print(f"Database error: {e}")
            self.db.rollback()
            return 0
        finally:
            self.db.close()
