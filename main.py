from asyncio import run
import os
from json import load
from aiogram import F, Bot, types, Dispatcher
from aiogram.filters import Command
from aiogram.types import FSInputFile
from song_processing.pars_song import parsing_song
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

TOKEN = config["Bot"]["token"]

bot = Bot(token=TOKEN)
dp = Dispatcher()

with open("data/data_for_message.json", "r") as file:
    data_for_message = load(file)


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(text=data_for_message["start"])


@dp.message(Command('find'))
async def start_search_the_song(message: types.Message):
    await message.answer(text=data_for_message["find"])


# TODO статусы
@dp.message(F.text)
async def search_the_song(message: types.Message):
    await message.answer("Ищем... Среднее время ожидания 1 минута")
    answer = parsing_song(message.text)
    if answer == "404":
        await message.answer(text=data_for_message["not_found"])
    elif answer == "OK":
        # получаем путь до песни
        directory = '/home/katrina/PycharmProjects/music_player/song_processing/song/'
        files = os.listdir(directory)
        filename = files[0]
        filepath = os.path.join(directory, filename)

        song = FSInputFile(filepath)
        await message.answer_audio(song, caption=f"Найдена песня: {filename[:-4]}")

# TODO извлечь метаданные из песни
# TODO добавить метаданные в базу данных и саму песню в вие байтов и удалить с компа


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main())
