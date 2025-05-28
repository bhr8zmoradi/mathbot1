import logging
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from telegram import ReplyKeyboardMarkup, KeyboardButton
# فعال کردن لاگینگ برای دیباگ راحت‌تر
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = "8095298226:AAE9bxIvC8yGnDqbN8zYlK_4DOFVRrLjZBM"
keyboard = [
    [KeyboardButton("📚 درس‌نامه"), KeyboardButton("📝 تمرین"), KeyboardButton("📊 آزمون")]
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
await update.message.reply_text(
    "سلام! خوش آمدی به ربات آموزش ریاضی.\nلطفاً یکی از گزینه‌های زیر را انتخاب کن:",
    reply_markup=reply_markup
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! خوش آمدی به ربات آموزش ریاضی.\n"
        "لطفاً یکی از گزینه‌های زیر را انتخاب کن:\n"
        "📚 درس‌نامه\n"
        "📝 تمرین\n"
        "📊 آزمون"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📚 درس‌نامه":
        await update.message.reply_text("""🔹 فصل: اعداد صحیح
🔸 جمع و تفریق اعداد صحیح:
برای جمع اعداد صحیح، علامت‌ها را بررسی می‌کنیم...""")

    elif text == "📝 تمرین":
        await update.message.reply_text("فعلاً تمرینی برای این بخش آماده نشده.")

    elif text == "📊 آزمون":
        await update.message.reply_text("فعلاً آزمونی برای این بخش آماده نشده.")

    else:
        await update.message.reply_text("لطفاً یکی از گزینه‌های منو را انتخاب کن.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("ربات در حال اجراست...")
    app.run_polling()

if __name__ == '__main__':
    main()
