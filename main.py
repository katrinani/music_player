from asyncio import run
from json import load
from aiogram import Bot, types, Dispatcher
from aiogram.filters import Command
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

TOKEN = config["Bot"]["token"]

bot = Bot(token=TOKEN)
dp = Dispatcher()

with open("data/data_for_message.json", "r") as file:
    data_for_message = load(file)


@dp.message(Command('start'))
async def choice_of_area(message: types.Message):
    await message.answer(text=data_for_message["start"])


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main())
