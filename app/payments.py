import stripe
from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from fastapi import APIRouter, Request
from app.bot import bot
from app.database.models import async_session, User
from sqlalchemy import select

import app.database.requests as rq

from config import WEBHOOK_SECRET, STRIPE_SECRET_KEY


router = APIRouter()

stripe.api_key = STRIPE_SECRET_KEY

PRODUCT_PRICE_ID = "price_1QviOcDFVaHAgzueaOyuoyAp"


async def buy_product(message: Message):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == message.from_user.id))

        if not user:
            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[{
                    "price": PRODUCT_PRICE_ID,
                    "quantity": 1
                }],
                mode="payment",
                success_url="https://www.google.com/",
                cancel_url="https://www.google.com/",
                metadata={
                    "chat_id": str(message.chat.id),
                    "tg_id": str(message.from_user.id)
                }
            )

            async def inline_keyboard(url):
                keyboard = InlineKeyboardBuilder()
                keyboard.add(InlineKeyboardButton(text="Pay", url=url))
                return keyboard.as_markup()

            await message.answer(text="Pay at link: ", reply_markup=await inline_keyboard(session.url))
        else:
            await message.answer("You already bought product!")


@router.post("/webhook")
async def webook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, WEBHOOK_SECRET)
    except Exception:
        return {"error": "Webhook error"}

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        chat_id = session["metadata"].get("chat_id")
        tg_id = session["metadata"].get("tg_id")
        await rq.add_user(int(tg_id))
        await bot.send_message(chat_id, text="✅ Payment successful!")

    return {"status": "succes"}