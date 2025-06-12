import telebot
import os
from flask import Flask, request

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return '', 200
    return 'ربات طلوع امید فعال است 💫'

# یک پیام تست برای مطمئن شدن از راه‌اندازی
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🌅 به ربات طلوع امید خوش اومدی!")

if __name__ == '__main__':
    app.run()
