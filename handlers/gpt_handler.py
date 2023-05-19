from telegram import Update

from chatgpt.chatgpt_api import chatCompletion
from telegram.ext import ContextTypes


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response_text = chatCompletion(update.message.text)

    dev_chat_id = context.bot_data["DEV_CHAT_ID"]
    await context.bot.send_message(
        dev_chat_id,
        f"Response from OpenAI: {response_text}!",
    )
