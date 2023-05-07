import telebot
import asyncio
from tok import*
import telegram
#from telegram import KeyboardButton, InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup #,ReplyKeyboardMarkup, KeyboardButton
from telebot import apihelper
import time
import os

TOKEN = tok()
# proxies = {'http': 'http://167.86.96.4:3128'}
# apihelper.proxy = proxies

bot = telebot.TeleBot(TOKEN)

# Создаем список с элементами для выбора
list = ['Элемент 1', 'Элемент 2']
# список кнопок
button_list = [
    InlineKeyboardButton("col1", callback_data=...),
    InlineKeyboardButton("col2", callback_data=...),
    InlineKeyboardButton("row 2", callback_data=...)
]

# # сборка клавиатуры из кнопок `InlineKeyboardButton`
# reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
# # отправка клавиатуры в чат для ВЕРСИИ 13.x
# bot.send_message(chat_id=chat_id, text="Меню из двух столбцов", reply_markup=reply_markup)

# @bot.message_handler(commands=['start'])
# def handle_start(message):
#     user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#     user_markup.row('1⃣ Начать 1⃣   ')
#     bot.send_message(message.from_user.id, 'Привет', reply_markup=user_markup)
def get_users():
    """
    Return users list

    In this example returns some random ID's
    """
    yield
@bot.message_handler(commands=['poll'])
def send_poll(message):
    bot.send_poll(message, 'вопрос', options=['1', '2', '3'])
# Создаем массив кнопок для отображения
keyboard = []
for item in list:
    keyboard.append([InlineKeyboardButton(item, callback_data=item,resize_keyboard=True, one_time_keyboard=True)])

# Создаем объект InlineKeyboardMarkup
reply_markup = InlineKeyboardMarkup(keyboard,row_width=1)
#print (reply_markup)
# Отправляем сообщение с клавиатурой
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, text="Выберите, что хотите улучшить?", reply_markup=reply_markup)
    return reply_markup
# Этот код создаст список "list", затем создаст массив кнопок "keyboard",
# который будет содержать каждый элемент списка в виде кнопки.
# Затем создается объект "InlineKeyboardMarkup",
# который используется для отправки сообщения с клавиатурой.



@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


# Обработка команд
@bot.message_handler(commands=['timer'])
def timer(message):
    for i in range(5):
        time.sleep(1)
        bot.send_message(message.chat.id, i + 1)


# Команда в параметром
@bot.message_handler(commands=['say'])
def say(message):
    # получить то что после команды
    text = ' '.join(message.text.split(' ')[1:])
    bot.reply_to(message, f'***{text.upper()}!***')


# Команда администратора
@bot.message_handler(commands=['admin'], func=lambda message: message.from_user.username == 'DanteOnline')
def admin(message):
    print(message)
    info = os.name
    bot.reply_to(message, info)


@bot.message_handler(commands=['admin2'])
def admin2(message):
    if message.from_user.username == 'DanteOnline':
        info = os.name
        bot.reply_to(message, info)
    else:
        bot.reply_to(message, 'Метод недоступен, нет прав')


@bot.message_handler(commands=['restart'])
def restart_server(message):
    # выполнить команду операционки из python
    # os.system('notepad')
    bot.reply_to(message, 'ура!')


@bot.message_handler(commands=['file'])
def get_file(message):
    print('зашел')
    # Передать какой то файл который есть на диске
    # with open('text.txt', 'r', encoding='utf-8') as data:
    #     bot.send_document(message.chat.id, data)
    with open('pict.jpg', 'rb') as data:
        bot.send_photo(message.chat.id, data)


@bot.message_handler(content_types=['text'])
def reverse_text(message):
    if 'плохой' in message.text.lower():
        bot.reply_to(message, 'В тексте слово плохой')
        return
    text = message.text[::-1]
    bot.reply_to(message, text)


@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    FILE_ID = 'CAADAgADPQMAAsSraAsqUO_V6idDdBYE'
    bot.send_sticker(message.chat.id, FILE_ID)

async def broadcaster() -> int:
    """
    Simple broadcaster

    :return: Count of messages
    """
    count = 0
    try:
        for user_id in get_users():
            # if await send_message(user_id, '<b>Hello!</b>'):
            #     count += 1
            print(user_id)
            await asyncio.sleep(.5)  # 20 messages per second (Limit: 30 messages per second)
    finally:
        log.info(f"{count} messages successful sent.")

    return count


bot.polling()




if __name__ == '__main__':
    # Execute broadcaster
    executor.start(dp, broadcaster())