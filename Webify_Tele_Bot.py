import telebot
from telebot import types

bot = telebot.TeleBot('5861935603:AAHIJlSDAEzcT0f9CVd_Onapzkb4EyCLdxM')

@bot.message_handler(commands=['start'])

def start(mes):
    bot.send_message(mes.chat.id, "Привет! \n функции: \n /start - начать \n /send_application - отправить заявку")
    
@bot.message_handler(commands=['send_application'])

def send_application(mes):  
    global application;
    while application == '': #проверяем что возраст изменился
        try:
            application = int(mes.text) #проверяем, что возраст введен корректно
        except Exception:
            bot.send_message(mes.from_user.id, 'Цифрами, пожалуйста');
            keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
            key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
            keyboard.add(key_yes); #добавляем кнопку в клавиатуру
            key_no= types.InlineKeyboardButton(text='Нет', callback_data='no');
            keyboard.add(key_no);
            bot.send_message(mes.from_user.id, "", reply_markup=keyboard)

bot.polling()