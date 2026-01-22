from aiogram import Bot, Dispatcher, F
from asyncio import run

from aiogram.enums import ParseMode

from commands import router as cmd_router
from translator_file import router as translator_router

from dotenv import load_dotenv
from os import getenv
load_dotenv()

from save_users import create_user

TOKEN = getenv('TOKEN')
async def main():
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    create_user()

    dp.include_router(cmd_router)
    dp.include_router(translator_router)

    await dp.start_polling(bot)
if __name__=='__main__':
    run(main())