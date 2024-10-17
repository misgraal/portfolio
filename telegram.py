import telebot
import config
from eventLib import event

bot = telebot.TeleBot(config.TELEGRAM_BOT_TOKEN)

events = event('event.txt')

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, message.chat.id)

def sendForm():
    while True:
        text = events.EventHandler('sendMessage')
        
        if text != "":
            text = text.replace("\enter/", "\n", -1)
            bot.send_message("727148312", text)
        
if __name__ == '__main__':
    from threading import Thread

    polling_thread = Thread(target=bot.polling)
    polling_thread.start()

    sendForm()