from aiogram import *
from decouple import config
import os
import random

kocmocs = 'fkf'
prirodas = 'prir'
luduna = 'lud'

bot = Bot(config('API_TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('Привет, я бот, который отправляет тебе фотографии из 3 категорий: "природа", "люди" и "космос". Мои команды: /start, /help')

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("Введите, например, 'выведи мне людей' или 'космос' или 'природа'")

@dp.message_handler(content_types=['text'])
async def ko(message: types.Message):
    user_text = message.text.lower()
    
    if 'космос' in user_text:
        image_files = [f for f in os.listdir(kocmocs) if f.lower().endswith('.jpg')]
        if image_files:
            random_filename = random.choice(image_files)
            with open(os.path.join(kocmocs, random_filename), 'rb') as file:
                await message.reply_photo(photo=file)
    
    elif 'природ' in user_text:
        image_files = [f for f in os.listdir(prirodas) if f.lower().endswith('.jpg')]
        if image_files:
            random_filename = random.choice(image_files)
            with open(os.path.join(prirodas, random_filename), 'rb') as file:
                await message.reply_photo(photo=file)
                
    elif 'люд' in user_text:
        image_files = [f for f in os.listdir(luduna) if f.lower().endswith('.jpg')]
        if image_files:
            random_filename = random.choice(image_files)
            with open(os.path.join(luduna, random_filename), 'rb') as file:
                await message.reply_photo(photo=file)
                
                
                    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)    