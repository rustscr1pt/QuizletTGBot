from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession
from entity_layer.states_enum import StatesEnum
from repository_layer.user_repository import UserRepository


class CallbackCardsTrainerFlipCondition(BaseFilter):
    async def __call__(self, callback_query: CallbackQuery, db: AsyncSession) -> bool:
        user_id = str(callback_query.from_user.id)
        try:
            user_repo = UserRepository(db)  # Inject middleware-provided db
            user_state = (await user_repo.get_user(user_id)).state
            return (
                callback_query.data.startswith("FLIP:")
                and user_state == StatesEnum.TRAINS_CARDS.value
            )
        except Exception as e:
            print(f"Error in CallbackCardsTrainerFlipCondition: {e}")
            return False


class CallbackCardsTrainerMarkStudiedCondition(BaseFilter):
    async def __call__(self, callback_query: CallbackQuery, db: AsyncSession) -> bool:
        user_id = str(callback_query.from_user.id)
        try:
            user_repo = UserRepository(db)
            user_state = (await user_repo.get_user(user_id)).state
            return (
                callback_query.data.startswith("MARK_STUDIED:")
                and user_state == StatesEnum.TRAINS_CARDS.value
            )
        except Exception as e:
            print(f"Error in CallbackCardsTrainerMarkStudiedCondition: {e}")
            return False


class CallbackCardsTrainerNextCondition(BaseFilter):
    async def __call__(self, callback_query: CallbackQuery, db: AsyncSession) -> bool:
        user_id = str(callback_query.from_user.id)
        try:
            user_repo = UserRepository(db)
            user_state = (await user_repo.get_user(user_id)).state
            return (
                callback_query.data.startswith("NEXT:")
                and user_state == StatesEnum.TRAINS_CARDS.value
            )
        except Exception as e:
            print(f"Error in CallbackCardsTrainerNextCondition: {e}")
            return False


class CallbackCardsTrainerExitCondition(BaseFilter):
    async def __call__(self, callback_query: CallbackQuery, db: AsyncSession) -> bool:
        user_id = str(callback_query.from_user.id)
        try:
            user_repo = UserRepository(db)
            user_state = (await user_repo.get_user(user_id)).state
            return (
                callback_query.data.startswith("EXIT:")
                and user_state == StatesEnum.TRAINS_CARDS.value
            )
        except Exception as e:
            print(f"Error in CallbackCardsTrainerNextCondition: {e}")
            return False
