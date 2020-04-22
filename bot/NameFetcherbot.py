import logging

from telegram.ext import Updater, CommandHandler

'''

To set up the log module import mogging is used

Command handlers

Bot design 
    1. First a set of command handlers are designed like start,echo,help 
    2. The main function is defined

Main function:
    1. A updater instance that gets the token use_context ) True
    2. A dispatcher to register the handlers




'''



#Commmand Handlers
def start(update,context):
    #update.message.reply_text('Hello! I am your name fetcher bot')
    with open("file.txt",encoding='utf-8') as f:
            update.message.reply_text(f.read())



def main():

    updater = Updater('1138658257:AAE41jXhhSqtWVzBPruO2ZFMz79nGMhdjEk',use_context=True)

    db = updater.dispatcher

    db.add_handler(CommandHandler("start",start)) # ("Command",callbackFunction)


    #db.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
