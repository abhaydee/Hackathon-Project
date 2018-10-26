from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from watson_developer_cloud import ConversationV1
import json

context = None



def start(bot, update):
    print('Received /start command')
    update.message.reply_text('Hi!')


def help(bot, update):
    print('Received /help command')
    update.message.reply_text('Help!')


def message(bot, update):
    print('Received an update')
    global context

    conversation = ConversationV1(username='#',  
                                  password='#',  
                                  version='#')

    
    response = conversation.message(
        workspace_id='#',  
        input={'text': update.message.text},
        context=context)
    print(json.dumps(response, indent=2))
    context = response['context']

    
    resp = ''
    for text in response['output']['text']:
        resp += text

    update.message.reply_text(resp)


def main():
   
    updater = Updater('613248609:AAH8jN6-QlqqaZ9Meq-_LyoBooH4iwBplVg')  

    
    dp = updater.dispatcher

   
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    
    dp.add_handler(MessageHandler(Filters.text, message))

    
    updater.start_polling()

   
    updater.idle()


if __name__ == '__main__':
    main()
