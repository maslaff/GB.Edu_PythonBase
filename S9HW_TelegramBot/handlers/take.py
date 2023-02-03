import random

from loader import dp
from aiogram.types import Message
import game


@dp.message_handler(commands=['exit'])
async def exit(message: Message):
    if message.from_user.id in game.total:
        game.total.pop(message.from_user.id)
        await message.answer('Как хочешь. Рады были видеть.\n/start для новой игры')


@dp.message_handler()
async def mes_game(message: Message):
    if message.from_user.id in game.total:
        count = message.text
        if count.isdigit():
            count = int(count)
            usr = message.from_user.id
            usr_data: dict = game.total[usr]
            if usr_data.get('set_max') == 'set':
                usr_data.update(on_table=count)
                usr_data.update(set_max=False)
                await message.answer(f"Прекрасно! Теперь на столе {count} конфет. Давай играть.\nБери конфеты...")
            elif 0 < count < 29:
                uname = usr_data.get('name')
                sweets = usr_data.get('on_table')
                sweets -= count
                if await check_win(message, usr, f"{uname} победил! Поздравляю!", sweets):
                    return
                await message.answer(f"{uname} взял {count} конфет и на столе осталось {sweets}\n"
                                     f'Теперь ход бота...')
                bot_take = sweets % 28-1 if sweets > 28 else sweets
                bot_take = bot_take if bot_take > 0 else random.randint(1, 28)
                sweets -= bot_take
                if await check_win(message, usr, "Виталий Бот победил! Поздравим его!", sweets):
                    return
                await message.answer(f'Бот Виталий взял {bot_take} конфет и '
                                     f'на столе осталось {sweets}\n'
                                     f'Теперь твой ход...')
                usr_data.update(on_table=sweets)
            else:
                if count < 1:
                    await message.answer('Если не хочешь играть, выход вон там -> /exit')
                elif count > 28:
                    await message.answer('Договаривались 28, куда столько потащил!?')
                else:
                    await message.answer('Что это такое?')
                return
            game.total.update((usr, usr_data))
        else:
            await message.answer(f'Введите число от 1 до 28')


async def check_win(message: Message, usr: int, text: str, ontable: int):
    if ontable <= 0:
        await message.answer(f"{text}\n/start для новой игры.")
        game.total.pop(usr)
        return True
    return False
