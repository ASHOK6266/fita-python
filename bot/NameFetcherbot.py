import logging

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#updater = Updater(token="",use_context=True)

OPINION = range(1)

def start(update, context):
    with open("file.txt",encoding='utf-8') as f:
        x = f.read()
    context.bot.send_message(chat_id=update.effective_chat.id,text=x)
#start_Handler = CommandHandler('start',start)
#dispatcher.add_handler(start_Handler)

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

#echo_handler = MessageHandler(Filters.text, echo)
#dispatcher.add_handler(echo_handler)

'''
def fetch(update,context):
    with open("file.txt",encoding='utf-8') as f:
         x = f.read()
    context.bot.send_message(chat_id=update.effective_chat.id,text=x)

fetch_Handler = CommandHandler('fetch',fetch)
dispatcher.add_handler(fetch_Handler)
'''

def opinion(update, context):
    user = update.message.from_user
    logger.info("Bio of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Thank you! I hope we can talk again some day.')

    return OPINION

def main():
    updater =  Updater("1138658257:AAEBVmaTh6sC9Ns858VfhCY-rSfKjhjLp0w",use_context=True)
    
    dp = updater.dispatcher
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start',start)],
        states = {
            OPINION : [MessageHandler(Filters.opinion),opinion]})


    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
