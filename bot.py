import os
import json
import random
from telegram import Bot
from openai import OpenAI

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CHANNEL_ID = "@WBXISmartStudy"

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found in secrets")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in secrets")

bot = Bot(token=BOT_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

def load_subjects():
    with open("subjects.json", "r", encoding="utf-8") as f:
        return json.load(f)

def generate_question(subject, language):
    prompt = f"""
    Generate one important Class 11 West Bengal Board question.
    Subject: {subject}
    Language: {language}
    Mention chapter name.
    Only output the chapter name and question.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

def create_post():
    subjects = load_subjects()
    message = "📚 WB XI Smart Study Zone\n\n"

    for subject, info in subjects.items():
        try:
            question = generate_question(subject, info["language"])

            message += f"📘 Subject: {subject}\n"
            message += f"🔥 Important Question:\n{question}\n\n"

        except Exception as e:
            message += f"❌ Error generating question for {subject}\n\n"

    bot.send_message(chat_id=CHANNEL_ID, text=message)

if __name__ == "__main__":
    create_post()
