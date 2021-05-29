import telebot

bot = telebot.TeleBot("1733620523:AAHyNGL7gl19bHHivSNmX0LaU8SrRLfw3U8")

@bot.message_handler(content_types=["text"])
def handle_text(message):
	if message.text == "Привет!":
		bot.send_message(message.from_user.id, "Приветик!")

	elif message.text == "Как ты?":
		bot.send_message(message.from_user.id, "Нормально")
	else:
		return 0;

bot.polling(none_stop=True, interval=0)