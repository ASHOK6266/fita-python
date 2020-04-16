from telegram.ext import Updater, CommandHandler
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token="1138658257:AAGrzbG6EWU60dt4vJ6XAeUH1ppv7r6oA30",use_context=True)

dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_Handler = CommandHandler('start',start)
dispatcher.add_handler(start_Handler)

updater.start_polling()
