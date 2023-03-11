import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message

API_TOKEN = '5844501317:AAEgTSj7cjzJct-ld5FPd8_2xgRik7OgNW8'

logging.basicConfig(level=logging.INFO)
bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def cmd_start(message: Message):
    await message.answer("Hi there! I'm a voice message filter bot.")

@dp.message_handler(content_types=['voice'])
async def voice_handler(message: Message):
    # download the voice message
    file = await bot.get_file(message.voice.file_id)
    await file.download('voice_message.ogg')

    # apply your filtering logic here
    # ...

    # send the filtered voice message back to the user
    with open('filtered_voice_message.ogg', 'rb') as f:
        await bot.send_voice(message.chat.id, f)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
