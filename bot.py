import os
import random
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@WBXISmartStudy"

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

questions = [
"Explain the main concept of this chapter.",
"Write a short note on the important topic of this chapter.",
"Describe the key features of this chapter.",
"What are the main ideas discussed in this chapter?",
"Explain the importance of this chapter in the syllabus.",
"Discuss the major points of this chapter.",
"Write the summary of this chapter.",
"Explain the main theory of this chapter."
]

def send_questions():
    
    bot = Bot(token=BOT_TOKEN)

    message = "📚 WB XI Smart Study Zone\n\n"

    for subject in subjects:

        question = random.choice(questions)

        message += f"📘 Subject: {subject}\n"
        message += f"🔥 Important Question:\n"
        message += f"{question}\n\n"

    bot.send_message(chat_id=CHANNEL_ID, text=message)

if __name__ == "__main__":
    send_questions()
