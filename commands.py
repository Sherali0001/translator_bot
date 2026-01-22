from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
import time

from save_users import insert_user, get_user

router = Router()


@router.message(Command('start'))
async def start(msg: Message):
    insert_user(
        telegram_id=msg.from_user.id,
        name=msg.from_user.first_name,
        username=msg.from_user.username
    )
    await msg.reply(text='Tarjimon botga xush kelibsiz! 😊')
    time.sleep(0.3)
    await msg.answer(text='Tilni sozlash uchun /choose buyruqni kiriting 🗝️')

@router.message(Command("watch"), F.from_user.id == 6584346083)
async def watch(msg: Message):
    rows = get_user()
    for user in rows:
        username = user[3]
        if username:
            username = f"@{username}"
        else:
            username = 'aniqlanmadi ❌'
        response = f"name: {user[1]},\nusername: {username},\nstart time: {user[2]}"
        await msg.answer(text=response)
        time.sleep(0.5)
    await msg.reply(text="⬆️ Ushbu foydalanuvchilar aniqlandi.")