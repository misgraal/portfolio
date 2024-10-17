import telebot
import config

bot = telebot.TeleBot(config.TELEGRAM_BOT_TOKEN)



# Optionally, this could be the bot's main function if you also run it as a bot.
def start_bot():
    @bot.message_handler(commands=["start"])
    def start(message):
        bot.send_message(message.chat.id, message.chat.id)

    def sendMessage(chat_id, text):
        bot.send_message(chat_id, text)
    # You can add your bot handlers here if needed
    bot.infinity_polling()

def send_message(chat_id, message_text):
    sendMessage()

if __name__ == "__main__":
    start_bot()