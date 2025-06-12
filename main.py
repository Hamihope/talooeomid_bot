import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

TOKEN = os.getenv("BOT_TOKEN", "8012107542:AAHr35D0rDqxW9PguqLBo_Y8pkFAjCo-m2U")
bot = telebot.TeleBot(TOKEN)

ADMIN_ID = 123456789  # اینجا عدد عددی آیدی عددی ادمین رو بذار

MIN_PAYMENT = 200000  # حداقل مبلغ پرداخت
ZARINPAL_LINK = "https://talooeomid.zarinp.al"
SUPPORT_ID = "@tl_omidSP"

users = {}

# دکمه‌های شروع
def main_menu():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("🎁 شرکت در قرعه‌کشی", callback_data="join"))
    markup.row(InlineKeyboardButton("📄 وضعیت من", callback_data="status"),
               InlineKeyboardButton("👥 معرفی به دوستان", callback_data="invite"))
    markup.row(InlineKeyboardButton("🆘 پشتیبانی", url=f"https://t.me/{SUPPORT_ID.replace('@','')}"))
    return markup

@bot.message_handler(commands=["start"])
def start_handler(message):
    user_id = message.from_user.id
    bot.send_message(user_id,
        f"سلام {message.from_user.first_name} 🌅\n"
        "به کمپین *طلوع امید* خوش اومدی!\n"
        "برای ورود به قرعه‌کشی بزرگ با جوایز موبایل، نقدی و سکه به ارزش ۲۰۰ میلیون تومان، دکمه زیر رو بزن.",
        reply_markup=main_menu(), parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "join":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id,
            f"برای شرکت در قرعه‌کشی باید حداقل مبلغ *۲۰۰٬۰۰۰ تومان* پرداخت کنید.\n"
            f"لینک پرداخت 👇\n{ZARINPAL_LINK}\n\n"
            "بعد از پرداخت، رسید خود را اینجا ارسال کنید.",
            parse_mode="Markdown")

    elif call.data == "status":
        bot.answer_callback_query(call.id)
        if call.from_user.id in users:
            bot.send_message(call.message.chat.id, "✅ پرداخت شما ثبت شده است. شما در قرعه‌کشی شرکت داده شدید.")
        else:
            bot.send_message(call.message.chat.id, "⛔ شما هنوز پرداختی انجام نداده‌اید.")

    elif call.data == "invite":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id,
            "برای دریافت شانس بیشتر، لینک ربات رو برای دوستانت بفرست:\n"
            "https://t.me/HamiOmid_bot")

@bot.message_handler(content_types=["text", "photo"])
def receipt_handler(message):
    if message.from_user.id in users:
        bot.reply_to(message, "✅ قبلاً رسید شما ثبت شده است.")
    else:
        users[message.from_user.id] = message.text
        bot.reply_to(message, "✅ رسید شما دریافت شد و پس از تأیید در قرعه‌کشی شرکت داده می‌شوید.")
        bot.send_message(ADMIN_ID, f"🔔 کاربر جدید:\n{message.from_user.first_name}\n\n📎 رسید:\n{message.text}")

# اجرای ربات
print("ربات با موفقیت اجرا شد.")
bot.infinity_polling()
