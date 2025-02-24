from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from app.payments import buy_product

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello! Welcome to bot.\n/buy")

@router.message(Command("buy"))
async def cmd_buy(message: Message):
    await buy_product(message)