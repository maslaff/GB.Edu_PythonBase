import game
from loader import dp
from aiogram.types import Message


@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    if message.from_user.id in game.total:
        await message.answer('Ты уже начал игру! Играй давай!')
    else:
        await message.answer(f'Привет, {message.from_user.full_name}!\n'
                             f'Мы будем играть в конфеты. На столе {game.max_total} конфет.\n'
                             '   Можно положить сколько хочешь конфет, отправив /put\n'
                             'Бери от 1 до 28...'
                             )
        game.total[message.from_user.id] = {
            'name': message.from_user.first_name,
            'on_table': game.max_total,
            'set_max': 'new'
        }
        print(f"{message.from_user.full_name} начал новую игру.")


@dp.message_handler(commands=['put'])
async def mes_max(message: Message):
    if message.from_user.id in game.total and \
            game.total[message.from_user.id].get('set_max') == 'new':
        await message.answer('Сколько бы ты хотел конфет на столе?')
        game.total[message.from_user.id].update(set_max='set')
        print(f"{message.from_user.full_name} решил изменить количество конфет.")
