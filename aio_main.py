import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from hendlers import bot_teleg


async def main():
    # bot = Bot(token="2040334276:AAH_uW2AZfIMa538tVujTTzNBvlHFjy_Y1c")
    bot = Bot(token="1919792326:AAGFxE4-qrRrooJb97YYrFNFDWCQLC3ANO4")
    url = 'mongodb+srv://Alise:gfccfnb@cluster0.wssfl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    storage = MongoStorage(uri=url)
    dp = Dispatcher(bot, storage=storage)
    # dp = Dispatcher(bot, storage=MemoryStorage())

    # Включаем логирование, чтобы не пропустить важные сообщения
    logging.basicConfig(level=logging.INFO)
    bot_teleg.register_handlers(dp)
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
