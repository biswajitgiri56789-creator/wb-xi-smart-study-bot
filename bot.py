import json
import random
import os
from telegram import Bot
from openai import OpenAI

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
CHANNEL_ID = "@WBXISmartStudy"

bot = Bot(token=BOT_TOKEN)
client = OpenAI(api_key=OPENAI_KEY)

def load_subjects():
    with open("subjects.json", "r", encoding="utf-8") as f:
        return json.load(f)

def load_posted():
    with open("posted_questions.json", "r", encoding="utf-8") as f:
        return json.load(f)

def save_posted(data):
    with open("posted_questions.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def generate_question(subject, language):
    prompt = f"""
    Generate one important Class 11 West Bengal Board question.
    Subject: {subject}
    Language: {language}
    Mention chapter name.
    Only question output. No explanation.
    Avoid repeating common generic questions.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

def create_post():
    subjects = load_subjects()
    posted = load_posted()
    message = "📚 WB XI Smart Study Zone\n\n"

    for subject, info in subjects.items():
        q = generate_question(subject, info["language"])

        if q in posted:
            continue

        posted.append(q)

        message += f"📘 Subject: {subject}\n"
        message += f"🔥 Important Question:\n{q}\n\n"

    save_posted(posted)
    bot.send_message(chat_id=CHANNEL_ID, text=message)

if __name__ == "__main__":
    create_post()