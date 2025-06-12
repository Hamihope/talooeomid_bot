import os
import telebot

# دریافت توکن از متغیر محیطی
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("توکن ربات پیدا نشد. لطفاً متغیر BOT_TOKEN را در تنظیمات Render وارد کن.")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! به ربات کمپین طلوع امید خوش اومدی ☀️")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "پیام شما دریافت شد 🌟")

print("ربات در حال اجراست...")
bot.infinity_polling()
