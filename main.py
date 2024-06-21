
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '7052135484:AAFtRHRqsWCSkE1Te4UPNBHx_0UIl-5s1nI'

BOT_USERNAME: Final = '@malpertuibot_bot'

# Команды
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Прив! Спасибо, что написали мне! Я тестовый бот Вовки. Просто игрушка для него в его могучих руках')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Напишите че-то, чтобы я смог ответить')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Это какая-то необычная команда')


#Ответы

# def handle_response(text: str) -> str:
def handle_response(text):

    # processed: str = text.lower()

    # if 'прив' or 'Прив' in processed:
    #     return 'Привітулі'
    # if 'как' or 'Как' in processed:
    #     return 'Нормально. Но не хватает немножко человеческих эмоций'
    # if 'какашка' or 'Какашка' in processed:
    #     return 'Самы ты какашка!'
    # else:
    #     return 'Непонятно нифига! По-человечески можешь общаться???'


    text = text.lower()

    if 'прив' in text:
        return 'Привітулі'
    if 'как' in text:
        return 'Нормально. Но не хватает немножко человеческих эмоций'
    if 'говно' in text:
        return 'Сам ты какашка!'
    else:
        return 'Непонятно нифига! По-человечески можешь общаться???'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
        message_type: str = update.message.chat.type
        text: str = update.message.text

        print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

        if message_type == 'group':
            if BOT_USERNAME in text: 
                new_text: str = text.replace(BOT_USERNAME, '').strip()
                response: str = handle_response(new_text)
            else:
                return
        else:
            response: str = handle_response(text)

        print('Bot', response)
        await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Начинаем...')
    app = Application.builder().token(TOKEN).build()


    #Команды
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #Сообщения
    app.add_handler(MessageHandler(filters.TEXT, handle_message))


    #Ошибки
    app.add_error_handler(error)
    print('Чё-то ниче не происходит...')
    app.run_polling(poll_interval=5)
