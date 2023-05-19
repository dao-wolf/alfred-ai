import html
import json
from logging import Logger
import traceback
from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    dev_chat_id = context.bot_data["DEV_CHAT_ID"]
    logger = context.bot_data["logger"]
    logger.info("Echo handler called")
    """Log the error and send a telegram message to notify the developer."""
    logger.error("Exception while handling an update:", exc_info=context.error)

    tb_list = traceback.format_exception(
        None, context.error, context.error.__traceback__
    )
    tb_string = "".join(tb_list)

    update_str = update.to_dict() if isinstance(update, Update) else str(update)
    message = (
        f"An exception was raised while handling an update\n"
        f"<pre>update = {html.escape(json.dumps(update_str, indent=2, ensure_ascii=False))}"
        "</pre>\n\n"
        f"<pre>context.chat_data = {html.escape(str(context.chat_data))}</pre>\n\n"
        f"<pre>context.user_data = {html.escape(str(context.user_data))}</pre>\n\n"
        f"<pre>{html.escape(tb_string)}</pre>"
    )
    await context.bot.send_message(dev_chat_id, text=message, parse_mode=ParseMode.HTML)
