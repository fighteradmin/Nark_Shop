import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import BotCommandScopeAllPrivateChats

from dotenv import find_dotenv, load_dotenv

from handlers.admin_private import admin_router
from handlers.user_group import user_group_router
from handlers.user_private import user_private_router
from common.bot_cmds_list import private

load_dotenv(find_dotenv())


bot = Bot(token=os.getenv('TOKEN'))
bot.my_admins_list = []
dp = Dispatcher()

dp.include_router(user_private_router)
dp.include_router(user_group_router)
dp.include_router(admin_router)


async def main():
    await bot.set_my_commands(commands=private, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)



asyncio.run(main())