import telebot
from telebot import *
import pyjokes_hebrew
keyboard1 = telebot.types.ReplyKeyboardMarkup()

bot = telebot.TeleBot('your-token')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello {message.from_user.first_name} ' f'{message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, reply_markup=keyboard1)


@bot.message_handler(commands=['PORN'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Enter the site', url='https://www.xvideos.com'))
    bot.send_message(message.chat.id, 'porn', reply_markup=markup)


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('enter the site', url='https://www.google.com'))
    bot.send_message(message.chat.id, 'google', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    start = types.KeyboardButton('/start')
    website = types.KeyboardButton('/website')
    porn = types.KeyboardButton('/PORN')
    markup.add(start, website, porn)
    bot.send_message(message.chat.id, 'choose to do', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if 'hello'in message.text:
        bot.send_message(message.chat.id, 'hey there! ,how are you?', reply_markup=keyboard1)

    elif 'good' in message.text:
        bot.send_message(message.chat.id, 'we glad to hear, what can i do for you?', reply_markup=keyboard1)

    elif 'id' in message.text:
        bot.send_message(message.chat.id, f'your ID is {message.from_user.id}', reply_markup=keyboard1)

    elif 'sad' in message.text:
        bot.send_message(message.chat.id, 'is a joke chear you up?', reply_markup=keyboard1)
        if message.text == 'yes' or 'yes please':
            bot.send_message(message.chat.id,pyjokes_hebrew.get_random_joke(),reply_markup = keyboard1)
        else:
            bot.send_message(message.chat.id,'i hope you feel better on your own way',reply_markup=keyboard1)
    elif 'joke' in message.text:
        bot.send_message(message.chat.id,pyjokes_hebrew.get_random_joke(),reply_markup = keyboard1)
        
    # else:
    #    bot.send_message(message.chat.id,'i dont understand',reply_markup=keyboard1)


bot.polling(none_stop=True)
