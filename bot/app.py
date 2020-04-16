import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def echo(update, context):
    """Echo the user message."""
    db = update.message.reply_text(update.message.text)




def main():
    updater = Updater("1138658257:AAGrzbG6EWU60dt4vJ6XAeUH1ppv7r6oA30",use_context=True)

    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text,echo))

    updater.start_pollling()

    updater.idle()

if __name__ == '__main__':
    main()