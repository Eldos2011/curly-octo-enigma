import telebot

bot = telebot.TeleBot("8121007149:AAFgYRQn5HNDolQQGVaBcL0U3RMjPdo5ehA")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "файылды алу үшін мына instagram парақшаға тіркел https://www.instagram.com/eldos_ka1ievv/profilecard/?igsh=eWczMmRjenoyZjZy" )
	
bot.polling()