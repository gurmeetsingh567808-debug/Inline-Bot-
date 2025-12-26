import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))

app = Client(
    "inline_dynamic_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

user_data = {}

@app.on_message(filters.private & filters.command("start"))
async def start(_, msg):
    await msg.reply(
        "🤖 Inline Maker Bot Ready\n\n"
        "👉 Photo + caption bhejo\n"
        "👉 Button text → link → channel ID"
    )

@app.on_message(filters.private & filters.photo)
async def photo_handler(_, msg):
    if msg.from_user.id != OWNER_ID:
        return await msg.reply("❌ Only owner allowed")

    user_data[msg.from_user.id] = {
        "photo": msg.photo.file_id,
        "caption": msg.caption or ""
    }

    await msg.reply("🔘 Button TEXT bhejo")

@app.on_message(filters.private & filters.text)
async def text_handler(_, msg):
    uid = msg.from_user.id
    if uid != OWNER_ID or uid not in user_data:
        return

    data = user_data[uid]

    if "btn_text" not in data:
        data["btn_text"] = msg.text
        return await msg.reply("🔗 Button LINK bhejo")

    if "btn_url" not in data:
        data["btn_url"] = msg.text
        return await msg.reply("📢 Channel ID ya @username bhejo")

    data["channel"] = msg.text.strip()

    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton(data["btn_text"], url=data["btn_url"])]]
    )

    await app.send_photo(
        chat_id=data["channel"],
        photo=data["photo"],
        caption=data["caption"],
        reply_markup=keyboard
    )

    user_data.pop(uid)
    await msg.reply("✅ Post channel me chala gaya")

app.run()