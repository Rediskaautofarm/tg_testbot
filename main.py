import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext, filters
from aiogram.types import Message, CallbackQuery, ChatType

TOKEN_Telegram = "5979393392:AAF_1lINfvaAO7GiVvMe8AjyU-xJ3uRh_IU"
client = Bot(TOKEN_Telegram, parse_mode="HTML")
dp = Dispatcher(client)

@dp.message_handler(content_types=['text'])
async def main(message: types.Message):
	content = str(message.text.lower()).split(" ")

	if content[0] == "!ping":
		await message.answer("test")


if __name__ == '__main__':
	print('работает')
	executor.start_polling(dp)