from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dev_chat_id = context.bot_data["DEV_CHAT_ID"]
    await context.bot.send_message(
        dev_chat_id,
        "Hi! I'm a bot integrated with ChatGPT. Type a message and I'll respond!",
    )
