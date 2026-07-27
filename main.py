from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
import os
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💎 Premium", callback_data="premium")]
    ]
    await update.message.reply_text(
        "👋 Welcome!",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
# Bot
    await query.edit_message_text("💎 Premium Price: ₹199")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
if __name__ == "__main__":
    app.run_polling()