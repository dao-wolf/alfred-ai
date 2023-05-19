import logging
import os
from pathlib import Path

import dotenv
from telegram import __version__ as TG_VER
from telegram.ext import (
    filters,
    MessageHandler,
    ApplicationBuilder,
    CommandHandler,
)
from handlers.gpt_handler import chat
from handlers.start_handler import start
from handlers.unknown_handler import unknown
from handlers.error_handler import error_handler

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )

dotenv.load_dotenv(Path.cwd() / ".env")
API_KEY = os.getenv("TELEGRAM_API_KEY")
DEV_CHAT_ID = os.getenv("DEVELOPER_CHAT_ID")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main() -> None:
    if not API_KEY:
        raise ValueError("TELEGRAM_API_KEY environment variable is missing")
    if not DEV_CHAT_ID:
        raise ValueError("DEV_CHAT_ID environment variable is missing")

    application = ApplicationBuilder().token(API_KEY).build()
    application.bot_data["DEV_CHAT_ID"] = DEV_CHAT_ID
    application.bot_data["logger"] = logger

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), chat))
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    # ...and the error handler
    application.add_error_handler(error_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
