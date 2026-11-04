import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")

MENU = [
    ["🎁 Daily Bonus", "💰 My Balance"],
    ["👥 Refer & Earn", "📋 Earn Tasks"],
    ["💸 Withdraw"],
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup(MENU, resize_keyboard=True)

    await update.message.reply_text(
        "👋 Welcome to Ayaz USDT Rewards Bot!\n\n"
        "Complete tasks and earn rewards.\n"
        "👇 Select an option below:",
        reply_markup=keyboard,
    )

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    messages = {
        "🎁 Daily Bonus": "🎁 Daily Bonus feature is coming soon!",
        "💰 My Balance": "💰 Your balance: 0.000 USDT",
        "👥 Refer & Earn": "👥 Referral system is coming soon!",
        "📋 Earn Tasks": "📋 Tasks will appear here soon!",
        "💸 Withdraw": "💸 Withdrawal system is coming soon!",
    }

    await update.message.reply_text(
        messages.get(
            update.message.text,
            "Please select an option from the menu.",
        )
    )

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN is not set!")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, menu_handler)
    )

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
