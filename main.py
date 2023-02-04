import telebot
from telebot import types

bot = telebot.TeleBot('5831467675:AAFXyP0ScBiLy7ozI3yq2spDrFq648dlXhQ')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Привет, я бот разработанный Лерой Чемековой,\n ты можешь написать мне"
                                               "имя любого художника, и я расскажу тебе о нём и покажу его работы")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("ДА")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Начнём ?', reply_markup=markup)
        bot.register_next_step_handler(message, artists_choice)
    print(message.text, end=' ')
    print(message.from_user.username)

# выбор художника
def artists_choice(message):
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    # добавь в массив types.InlineKeyboardButton(text='Леонардо да Винчи', callback_data='leonardo') только измени text
    # и callback_data последнее как раз писать в условии ввывода информации
    artist = [types.InlineKeyboardButton(text='Леонардо да Винчи', callback_data='leonardo'),
              types.InlineKeyboardButton(text='Микелянджело', callback_data='mik')]
    for i in artist:
        keyboard.add(i)
    bot.send_message(message.from_user.id, text='Выбери художника', reply_markup=keyboard)
    print(message.text, end=' ')
    print(message.from_user.username)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    #Вывод информации о художниках
    print(call.data, end=' ')
    print(call.message.from_user.username)
    if call.data == "leonardo":
        info = 'Леонардо да Винчи - итальянский художник (живописец, скульптор, архитектор)' \
               ' и учёный (анатом, естествоиспытатель), изобретатель, писатель, музыкант, один из крупнейших ' \
               'представителей искусства Высокого Возрождения, яркий пример «универсального человека»'

        bot.send_message(call.message.chat.id, text=info)
        bot.send_message(call.message.chat.id, text='вот парачка его работ:')
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('data/мона лиза.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('data/2.jpg', 'rb'))])
        # заного запускать выбор художника
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("ДА")
        markup.add(item1)
        bot.send_message(call.message.chat.id, 'Ещё раз ?', reply_markup=markup)
        bot.register_next_step_handler(call.message, artists_choice)
    elif call.data == 'mik':
        pass

bot.polling(none_stop=True, interval=0)
