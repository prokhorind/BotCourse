import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message

# Set up logging
logging.basicConfig(level=logging.INFO)

# Your bot token from BotFather
API_TOKEN = os.environ.get("API_TOKEN")

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Echo handler - responds with the same text the user sends
async def echo(message: Message):
    print(message.model_dump_json(indent=4))
    await message.answer(message.text)

async def init():
    dp.message.register(echo)

    await dp.start_polling(bot)



if __name__ == '__main__':
    # Start the bot
    asyncio.run(init())