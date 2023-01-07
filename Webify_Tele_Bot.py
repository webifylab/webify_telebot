import telebot

bot = telebot.TeleBot('5610222750:AAEWIgLAxyFGJFLy4eGDkJq0bvrAE_YA4WA')

@bot.message_handler(commands=['start'])
def start(mes):
    bot.send_message(
        mes.chat.id,    
        '<b>Привет!</b>' , 
        parse_mode="html"
    )

bot.polling(none_stop=True)