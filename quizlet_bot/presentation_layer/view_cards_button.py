from aiogram import Router, F
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession
from service_layer.card_service import CardService
from ui_layer.start_command_keyboards import StartCommandKeyboards
from utilities.message_chunker import chunk_message

router = Router()


@router.message(F.text == "View Cards")
async def handle_view_cards_button(message: Message, db: AsyncSession):
    card_service = CardService(db)
    user_id = str(message.from_user.id)

    user_cards = await card_service.get_user_cards(user_id)

    if user_cards:
        response = "<b>Ваши добавленные карты:</b>\n\n"
        for index, card in enumerate(user_cards):
            response += f"{index + 1})\n<b>Аверс:</b> {card.front_side}\n<i>Реверс:</i> {card.back_side}\n\n"
        message_chunks = chunk_message(response)
        for i, chunk in enumerate(message_chunks):
            if i == len(message_chunks) - 1:
                await message.answer(
                    chunk, reply_markup=StartCommandKeyboards.startup_card_builder()
                )
            else:
                await message.answer(chunk)
    else:
        await message.answer(
            "You don't have any cards yet. Use the 'Create Cards' button to add new cards.",
            reply_markup=StartCommandKeyboards.startup_card_builder(),
        )
