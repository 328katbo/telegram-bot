from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "7009379539:AAERI93iD6oAbzkqL9eEKcthUJww7Ku-dgw"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я работаю!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
