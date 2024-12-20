import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
# Включаем логирование, чтобы не пропустить важные сообщения
#logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="8146118632:AAHd-SzQfPvUx1Z6jTqPpGDeMTBV5Rin9kw")
# Диспетчер
dp = Dispatcher()
me = []
user_list = ['@Terc1a', '@onenoxion']

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message(Command("ping"))
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text='Click me daddy',
        callback_data="clicked"
    )
    )
    to_ping = '\n'.join(user_list)
    iam = message.from_user.first_name
    me.append(iam)
    await message.answer(to_ping, reply_markup=builder.as_markup())

@dp.callback_query(F.data == "clicked")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(f'Хули тыкаешь {callback.from_user.username}')

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())