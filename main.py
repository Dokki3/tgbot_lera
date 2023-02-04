import telebot

bot = telebot.TeleBot('5831467675:AAFXyP0ScBiLy7ozI3yq2spDrFq648dlXhQ')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "привет" or message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
    print(message.text, end=' ')
    print(message.from_user.username)


bot.polling(none_stop=True, interval=0)
