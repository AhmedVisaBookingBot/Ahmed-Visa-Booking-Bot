import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "أهلاً بيك 👋\n"
        "بوت أحمد لحجز ومتابعة مواعيد التأشيرات 🇮🇹\n\n"
        "البوت شغال بنجاح ✅"
    )

@bot.message_handler(commands=["help"])
def help_command(message):
    bot.reply_to(
        message,
        "الأوامر المتاحة:\n"
        "/start - تشغيل البوت\n"
        "/help - المساعدة"
    )

bot.infinity_polling()
