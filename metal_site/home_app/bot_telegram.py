from aiogram import Bot, Dispatcher

from metal_site.secret import TG_KEY


TOKEN, CHAT_ID, ADMIN_ID = TG_KEY

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def send_telegram_message(message):
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message)
    except Exception as err:
        await bot.send_message(chat_id=ADMIN_ID, text=err)
    pass
