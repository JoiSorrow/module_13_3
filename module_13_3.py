from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7764276027:AAHE81bthYw3FBnipz3S9aZc-R3IPg1qURk"
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

@dp.message_handler(text = ['/start'])
async def start(message):
    print('Привет! Я - бот, помогающий твоему здоровью.')
    await message.answer('Привет! Я - бот, помогающий твоему здоровью.')

@dp.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)




