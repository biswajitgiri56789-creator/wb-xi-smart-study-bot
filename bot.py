import os
import random
from telegram import Bot
from openai import OpenAI

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

CHANNEL_ID = "@WBXISmartStudy"

client = OpenAI(api_key=OPENAI_API_KEY)

subjects = [
"বাংলা",
"Physics",
"Chemistry",
"Biology",
"Mathematics",
"English",
"Computer Science",
"History",
"Geography",
"Political Science",
"Philosophy",
"Education",
"Sanskrit",
"Accountancy",
"Business Studies",
"Economics"
]

def generate_question(subject):

    prompt = f"""
Generate one important Class 11 exam question from the subject {subject}.
Only give the question.
Do not give answer.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def send_questions():

    bot = Bot(token=BOT_TOKEN)

    message = "📚 WB XI Smart Study Zone\n\n"

    for subject in subjects:

        question = generate_question(subject)

        message += f"📘 Subject: {subject}\n"
        message += f"🔥 Important Question:\n"
        message += f"{question}\n\n"

    bot.send_message(chat_id=CHANNEL_ID, text=message)


if __name__ == "__main__":
    send_questions()
