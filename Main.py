from Wolfram import WolframSearcher
from flask import Flask, request
import telebot
import os

searcher = WolframSearcher('AKGAVW-QYGPGY96AQ')
TOKEN = "1400971205:AAE3J8h2ku1ZmNbqpklnDjAYGBX0VX1EsyE"
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """
    Outputs a welcome message to the user

    Args:
        message {String}: The message that the user wrote
    """
    bot.reply_to(message, 'Welcome to Wolfram Alpha bot!')
    
@bot.message_handler(commands=['help'])
def show_commands(message):
    """
    Explains how to use the bot

    Args:
        message {String}: The message that the user wrote
    """
    string = "In order to use this bot, you need to pass a mathematical expresion with the values, or you can also search anything you need to know"
    bot.reply_to(message, string)
        
@bot.message_handler(func=lambda msg: msg.text is not None)
def search_Wolfram(message):
    """
    Seachs the message provided by the user on Wolfram and the outputs the answer

    Args:
        message {String}: The message that the user wrote
    """
    text = message.text
    bot.reply_to(message, searcher.search(text))
    
@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://your_heroku_project.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
