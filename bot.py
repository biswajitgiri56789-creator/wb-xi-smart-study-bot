import os
import json
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@WBXISmartStudy"

def load_subjects():
    try:
        with open("subjects.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {
            "Physics": {"language": "Bengali"},
            "Chemistry": {"language": "Bengali"},
            "Mathematics": {"language": "Bengali"}
        }

def create_post():
    if not BOT_TOKEN:
        print("BOT_TOKEN not found")
        return

    bot = Bot(token=BOT_TOKEN)
    subjects = load_subjects()

    message = "📚 WB XI Smart Study Zone\n\n"

    for subject in subjects:
        message += f"📘 Subject: {subject}\n"
        message += "🔥 Important Question:\n"
        message += "Sample Question Generated Successfully ✅\n\n"

    try:
        bot.send_message(chat_id=CHANNEL_ID, text=message)
        print("Message sent successfully")
    except Exception as e:
        print("Telegram Error:", e)

if __name__ == "__main__":
    create_post()
