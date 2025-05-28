import json
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from config import BOT_TOKEN

with open("lessons.json", "r", encoding="utf-8") as f:
    lessons = json.load(f)

user_data = {}
quiz_scores = {}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.effective_user.id
    chapter = "اعداد صحیح"

    if user_id not in user_data:
        user_data[user_id] = {"mode": None, "index": 0}

    if text == "/start":
        keyboard = [["📘 درسنامه", "📝 تمرین"], ["📊 آزمون"]]
        await update.message.reply_text(
            "به ربات آموزش ریاضی خوش آمدید!\nیکی از گزینه‌ها را انتخاب کنید:",
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        )
        user_data[user_id] = {"mode": None, "index": 0}

    elif text == "📘 درسنامه":
        await update.message.reply_text(lessons[chapter]["درسنامه"])
        user_data[user_id] = {"mode": None, "index": 0}

    elif text == "📝 تمرین":
        user_data[user_id]["mode"] = "exercise"
        user_data[user_id]["index"] = 0
        question = lessons[chapter]["تمرین"][0]["سؤال"]
        await update.message.reply_text(f"✏️ تمرین اول:\n\n{question}")

    elif user_data[user_id]["mode"] == "exercise":
        i = user_data[user_id]["index"]
        correct_answer = lessons[chapter]["تمرین"][i]["پاسخ"]
        if text.strip() == correct_answer:
            await update.message.reply_text("✅ درست بود!")
        else:
            await update.message.reply_text(f"❌ اشتباه بود! جواب درست: {correct_answer}")

        user_data[user_id]["index"] += 1
        i = user_data[user_id]["index"]

        if i < len(lessons[chapter]["تمرین"]):
            question = lessons[chapter]["تمرین"][i]["سؤال"]
            await update.message.reply_text(question)
        else:
            await update.message.reply_text("🏁 تمرین‌ها تمام شد.")
            user_data[user_id] = {"mode": None, "index": 0}

    elif text == "📊 آزمون":
        user_data[user_id]["mode"] = "quiz"
        user_data[user_id]["index"] = 0
        quiz_scores[user_id] = 0
        question = lessons[chapter]["آزمون"][0]["سؤال"]
        await update.message.reply_text(f"🧪 آزمون شروع شد!\n\n{question}")

    elif user_data[user_id]["mode"] == "quiz":
        i = user_data[user_id]["index"]
        correct_answer = lessons[chapter]["آزمون"][i]["پاسخ"]
        if text.strip() == correct_answer:
            quiz_scores[user_id] += 1
            await update.message.reply_text("✅ درست بود!")
        else:
            await update.message.reply_text(f"❌ اشتباه بود! جواب درست: {correct_answer}")

        user_data[user_id]["index"] += 1
        i = user_data[user_id]["index"]

        if i < len(lessons[chapter]["آزمون"]):
            question = lessons[chapter]["آزمون"][i]["سؤال"]
            await update.message.reply_text(question)
        else:
            score = quiz_scores[user_id]
            await update.message.reply_text(f"🏁 آزمون تمام شد!\nنمره‌ی شما: {score} از 5")
            user_data[user_id] = {"mode": None, "index": 0}

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
