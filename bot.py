import os
import threading
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ------------------ ENV VARIABLES ------------------ #

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))

# Render automatically provides this
RENDER_URL = os.getenv("RENDER_EXTERNAL_URL")
PORT = int(os.getenv("PORT", 10000))

# ------------------ FAKE HTTP SERVER ------------------ #

def run_http_server():
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Bot is running")

        def log_message(self, format, *args):
            return  # silence logs

    server = HTTPServer(("0.0.0.0", PORT), Handler)
    server.serve_forever()

# Run HTTP server in background
threading.Thread(target=run_http_server, daemon=True).start()

# ------------------ SELF PING FUNCTION ------------------ #

def self_ping():
    if not RENDER_URL:
        return
    try:
        requests.get(RENDER_URL, timeout=3)
    except:
        pass

# ------------------ TELEGRAM BOT ------------------ #

app = Client(
    "inline_dynamic_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

user_data = {}

@app.on_message(filters.private & filters.command("start"))
async def start(_, msg):
    self_ping()
    await msg.reply(
        "🤖 Inline Maker Bot Ready\n\n"
        "👉 Photo + caption bhejo\n"
        "👉 Button text → link → channel ID"
    )

@app.on_message(filters.private & filters.photo)
async def photo_handler(_, msg):
    self_ping()

    if msg.from_user.id != OWNER_ID:
        return await msg.reply("❌ Only owner allowed")

    user_data[msg.from_user.id] = {
        "photo": msg.photo.file_id,
        "caption": msg.caption or ""
    }

    await msg.reply("🔘 Button TEXT bhejo")

@app.on_message(filters.private & filters.text)
async def text_handler(_, msg):
    self_ping()

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

    try:
        await app.send_photo(
            chat_id=data["channel"],
            photo=data["photo"],
            caption=data["caption"],
            reply_markup=keyboard
        )
        await msg.reply("✅ Post channel me chala gaya")
    except Exception as e:
        await msg.reply(f"❌ Error:\n`{e}`")

    user_data.pop(uid)

# ------------------ RUN BOT ------------------ #

print("Bot started successfully")
app.run()