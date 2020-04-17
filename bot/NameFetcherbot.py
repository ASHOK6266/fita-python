from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#updater = Updater(token="",use_context=True)

dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_Handler = CommandHandler('start',start)
dispatcher.add_handler(start_Handler)

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

def fetch(update,context):
    with open("file.txt",encoding='utf-8') as f:
         x = f.read()
    context.bot.send_message(chat_id=update.effective_chat.id,text=x)

fetch_Handler = CommandHandler('fetch',fetch)
dispatcher.add_handler(fetch_Handler)

def main():
    updater =  Updater("",use_context = True)

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start',start)],

        states =  {
            GENDER : [MessageHandler(),]
            
        }
    )


updater.start_polling()


if __name__ == '__main__':
    main()
