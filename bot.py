import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()


@router.message(Command(commands=['start', 'help']))
async def send_welcome(message: Message):
    await message.answer("Привет. Это бот создан для оповещений по обращениям в компанию ЦИФРАЗ")


@router.message(F.text)
async def echo(message: Message):
    await message.answer("Данный бот создан исключительно для оповещений по обращениям")


dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
