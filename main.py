import config
import telebot

bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(content_types=('text'))
def moi_kofe_bot(message):
	bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True, timeout=100)