

from telegram import bot
from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler

#creating an Update object
updater = Updater(token="insert you telegram bot token here", use_context=True)

#locally intoducing dispatcher for quicker access
dispatcher = updater.dispatcher


#logging module
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#defining a function that should process a specific type of update
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Greetings traveler! This bot will encrypt your message for you using prime number encryption. Type /info for more information!")

#react on command like "start"
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def info(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="This bot randomly generates two prime numbers that are used to create keys for encryption and uses them to convert your message to one of the safest cyphers known to humanity. To encrypt you message print /prime <your number> or use /crypto_info to get more information about Prime Number encryption.")

#react on command like "start"
info_handler = CommandHandler('info', info)
dispatcher.add_handler(info_handler)


def crypto_info(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="https://www.abc.net.au/news/science/2018-01-20/how-prime-numbers-rsa-encryption-works/9338876")

#react on command like "start"
info_handler = CommandHandler('crypto_info', crypto_info)
dispatcher.add_handler(info_handler)


#testing other commands
#def echo(update, context):
#    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
#
from telegram.ext import MessageHandler, Filters
#echo_handler = MessageHandler(Filters.text, echo)
#dispatcher.add_handler(echo_handler)


from PrimeNumGFG import rsa
def caps(update, context):
    message = ' '.join(context.args)
    message = int(message)
    #message += 5

    messageg = str(rsa(message))

    context.bot.send_message(chat_id=update.effective_chat.id, text=messageg)


caps_handler = CommandHandler('prime', caps)
dispatcher.add_handler(caps_handler)




#importing unknown_response to unswer to commands that are not supported by bot
#has to be added last to not be trigger before CommandHandlers
from unknow_response import unknown
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

#testing custom filter
#import filter_test
#filter_awesome = filter_test.FilterAwesome()
#awesome_handler = MessageHandler(filter_awesome, callback)

import telebot

#tb = telebot.AsyncTeleBot("1034595570:AAFw-kBGT17WKJR-hiPwX49l9oqHQmKyd0k")
#task = tb.get_me() # Execute an API call
# Do some other operations...
#a = 0
#for a in range(100):
#	a += 10

#result = task.wait()

#tb = telebot.AsyncTeleBot("1034595570:AAFw-kBGT17WKJR-hiPwX49l9oqHQmKyd0k")
#def handle_messages(messages):
#	for message in messages:
#		# Do something with the message
#		telebot.reply_to(message, 'Hi')

#bot.set_update_listener(handle_messages)
#bot.polling()
#updates = bot.get_updates()
#print([u.message.text for u in updates])

#dispatcher.add_error_handler(error_callback)
updater.start_polling()