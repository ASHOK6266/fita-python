import logging

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler,dispatcher)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#updater = Updater(token="",use_context=True)

PHOTO = range(1)

def main():
    updater =  Updater("",use_context=True)
    
    dp = updater.dispatcher
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start',start)],
        states = {
            PHOTO: [MessageHandler(Filters.photo, photo),
                    CommandHandler('skip', skip_photo)],},
                    fallbacks=[CommandHandler('cancel', cancel)])


    updater.start_polling()

    updater.idle()


def start(update, context):
    with open("file.txt",encoding='utf-8') as f:
        x = f.read()
    context.bot.send_message(chat_id=update.effective_chat.id,text=x)
    start_Handler = CommandHandler('start',start)
    dispatcher.add_handler(start_Handler)

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
#echo_handler = MessageHandler(Filters.text, echo)
#dispatcher.add_handler(echo_handler)

def fetch(update,context):
    with open("file.txt",encoding='utf-8') as f:
         x = f.read()
    context.bot.send_message(chat_id=update.effective_chat.id,text=x)

    fetch_Handler = CommandHandler('fetch',fetch)
    dispatcher.add_handler(fetch_Handler)


def photo(update, context):
    user = update.message.from_user
    photo_file = update.message.photo[-1].get_file()
    photo_file.download('user_photo.jpg')
    logger.info("Photo of %s: %s", user.first_name, 'user_photo.jpg')
    update.message.reply_text('Gorgeous! Now, send me your location please, '
                              'or send /skip if you don\'t want to.')
    return PHOTO

def skip_photo(update, context):
    user = update.message.from_user
    logger.info("User %s did not send a photo.", user.first_name)
    update.message.reply_text('I bet you look great! Now, send me your location please, '
                              'or send /skip.')

    return Hello

def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END



if __name__ == '__main__':
    main()
