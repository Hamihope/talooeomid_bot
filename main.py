import telebot

# توکن ربات
TOKEN = '8012107542:AAFuosyvKUE6q4Ht4jBf3VV2ezxNCMxbh8U'
bot = telebot.TeleBot(TOKEN)

# پیام خوش‌آمد
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "🌅 سلام! به کمپین قرعه‌کشی «طلوع امید» خوش اومدی!\n\n"
        "🎁 با پرداخت حداقل ۲۰۰ هزار تومان وارد قرعه‌کشی شو\n"
        "🎉 جوایز مرحله اول: موبایل، پول نقد و سکه طلا (۲۰۰ میلیون تومان)\n\n"
        "برای ثبت‌نام روی لینک زیر کلیک کن:\n"
        "🔗 https://talooeomid-bot-2.onrender.com\n\n"
        "پشتیبانی: @tl_omidSP\n"
        "📞 تماس: 09357632421"
    )

# اجرای دائمی ربات
bot.infinity_polling()
