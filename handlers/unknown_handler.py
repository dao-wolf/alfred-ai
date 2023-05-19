from telegram import Update
from telegram.ext import ContextTypes


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dev_chat_id = context.bot_data["DEV_CHAT_ID"]
    await context.bot.send_message(
        dev_chat_id,
        "Sorry, I didn't understand that command.",
    )
