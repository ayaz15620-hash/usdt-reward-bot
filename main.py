
import os

from telegram import (
    Update,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")

# Your Force Join Channel
CHANNEL_USERNAME = "@Ayaz_USDT_Official"
CHANNEL_LINK = "https://t.me/Ayaz_USDT_Official"

MENU = [
    ["🎁 Daily Bonus", "💰 My Balance"],
    ["👥 Refer & Earn", "📋 Earn Tasks"],
    ["💸 Withdraw"],
]


async def check_membership(user_id, context):
    """Check whether the user has joined the required channel."""
    try:
        member = await context.bot.get_chat_member(
            CHANNEL_USERNAME,
            user_id,
        )
        return member.status not in ("left", "kicked")
    except Exception:
        return False


async def send_join_message(message):
    """Show the Force Join buttons."""
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "📢 Join Our Channel",
                url=CHANNEL_LINK,
            )
        ],
        [
            InlineKeyboardButton(
                "✅ I Have Joined",
                callback_data="check_join",
            )
        ],
    ])

    await message.reply_text(
        "📢 To use this bot, please join our official channel
