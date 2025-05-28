from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from config import TOKEN
import json

# بارگذاری فایل JSON
with open("lessons.json", "r", encoding="utf-8") as f:
    lessons = json.load(f)

# تعریف کیبورد
main_menu = [["📘 درس‌نامه", "📝 تمرین"], ["🧪 آزمون"]]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    chapter = "اعداد صحیح"

    if text == "/start":
        await update.message.reply_text(
            "سلام! به ربات آموزش ریاضی خوش اومدی ✨\nیک گزینه رو انتخاب کن:",
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
        )
    elif text == "📘 درس‌نامه":
        await update.message.reply_text(lessons[chapter]["درس‌نامه"])
    elif text == "📝 تمرین":
        for exercise in lessons[chapter]["تمرین‌ها"]:
            await update.message.reply_text(exercise)
    elif text == "🧪 آزمون":
        for q in lessons[chapter]["آزمون"]:
            question_text = f"{q['سؤال']}\n" + "\n".join([f"- {opt}" for opt in q["گزینه‌ها"]])
            await update.message.reply_text(question_text)
    else:
        await update.message.reply_text("گزینه‌ی نامعتبر! لطفاً از منو انتخاب کن.")

# راه‌اندازی ربات
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))

if __name__ == "__main__":
    app.run_polling()
