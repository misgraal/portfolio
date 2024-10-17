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
    # Use threading to run both polling and sending repetitive messages concurrently
    from threading import Thread

    # Start the polling loop in a separate thread
    polling_thread = Thread(target=bot.polling)
    polling_thread.start()

    # Start the repetitive message sending loop in the main thread or another thread
    sendForm()