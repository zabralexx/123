import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties

API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Открыть сайт",
            web_app=WebAppInfo(url="https://contribution-aggregator.org")
        )]
    ])
    await message.answer("Нажми на кнопку ниже, чтобы открыть сайт:", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
