import random

from loader import dp
from aiogram.types import Message
import game


@dp.message_handler()
async def mes_game(message: Message):
    for duel in game.total:

        if message.from_user.id == duel[0]:

            count = message.text
            if count.isdigit():
                if game.total[3]:
                    game.total[2] = int(count)
                    game.total[3] = False
                    await message.answer(f"Прекрасно! Теперь на столе {count} конфет. Давай играть.")
                elif 0 < int(count) < 29:
                    duel[2] -= int(count)
                    if await check_win(message, 'Ты', duel):
                        return True
                    await message.answer(f'{duel[1]} взял {count} конфет и на столе осталось {duel[2]}\n'
                                         f'Теперь ход бота...')
                    bot_take = duel[2] % 28-1 if duel[2] > 28 else duel[2]
                    bot_take = bot_take if bot_take > 0 else random.randint(
                        1, 28)
                    duel[2] -= bot_take
                    if await check_win(message, 'Бот', duel):
                        return True
                    await message.answer(f'Бот Виталий взял {bot_take} конфет и '
                                         f'на столе осталось {duel[2]}\n'
                                         f'Теперь твой ход...')
            else:
                await message.answer(f'Введите число от 1 до 28')


async def check_win(message: Message, win: str, duel: list):
    if duel[2] <= 0:
        await message.answer(f'{win} победил! Поздравляю!')
        game.total.remove(duel)
        return True
    return False
