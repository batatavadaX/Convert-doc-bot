import os

from pyrogram import Client, filters
from pyrogram.types import Message

BOT_TOKEN = os.environ.get('BOT_TOKEN')
APP_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH')

m = Client("m", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@m.on_message(filters.command("d", prefixes="/"))
async def send(Client, m: Message):
    try:
        k = await Client.download_media(message=message.reply_to_message, progress=progress)
        await m.send_document(message.chat.id, k, progress=progress)
    except Exception as e:
        await message.reply(message.chat.id, e)

async def progress(current, total):
    await message.edit(f"{current * 100 / total:.1f}%")

m.run()
