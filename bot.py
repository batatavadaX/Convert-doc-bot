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
        current = ""
        k = await Client.download_media(message=m.reply_to_message, progress=await m.edit(f"{current * 100 / total:.1f}%"))
        await Client.send_document(m.chat.id, k, progress=await m.edit(f"{current * 100 / total:.1f}%"))
    except Exception as e:
        await m.reply(e)

m.run()
