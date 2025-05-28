from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8095298226:AAE9bxIvC8yGnDqbN8zYlK_4DOFVRrLjZBM"  # توکن رباتت رو اینجا بذار

main_menu = [["📚 درس‌نامه"], ["📝 تمرین"], ["🧪 آزمون"], ["❓ سوال‌های شما"]]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! به ربات آموزش ریاضی خوش اومدی 🎓",
        reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "📚 درس‌نامه":
        await update.message.reply_text("فعلاً فقط درس‌نامه‌ی نمونه داریم")
("
🔹 فصل: اعداد صحیح
🔸 جمع و تفریق اعداد صحیح:
برای جمع اعداد صحیح، علامت‌ها را بررسی می‌کنیم...")
    elif text == "📝 تمرین":
        await update.message.reply_text("تمرین‌ها به‌زودی اضافه می‌شن.")
    elif text == "🧪 آزمون":
        await update.message.reply_text("آزمون آماده نیست هنوز.")
    elif text == "❓ سوال‌های شما":
        await update.message.reply_text("لطفاً سوالتون رو بفرستین. به‌زودی پاسخ داده می‌شه.")
    else:
        await update.message.reply_text("گزینه‌ای از منو انتخاب کن 🌟")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("ربات در حال اجراست...")
    app.run_polling()

if __name__ == "__main__":
    main()
