import logging
from tok import*
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler,Application

TOKEN=tok()
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

list = [['Элемент 1',5], ['Элемент 2',6]]
better=0
worse=0
# async def tab(update,_):
#     better=kbd1(update,_)
#     worse=kbd1(update,_)
#     update.message.reply_text(text=f"Улучшаем: {better}" "Ухудшается: {worse}")
async def tab(update, _):
    keyboard1=[]
    for but,call in list:
        keyboard1.append([InlineKeyboardButton(but, callback_data=call)])
    reply_markup = InlineKeyboardMarkup(keyboard1)
    await update.message.reply_text('Что хотите улучшить?:', reply_markup=reply_markup)

    #update.message.reply_text(text=f"Улучшаем: {better}  Ухудшается: {worse}")
async def button(update, _):
    query = update.callback_query
    variant = query.data
    better=query.data
    await query.answer()
    #await query.edit_message_text(text=f"Выбранный вариант: {variant}")
    return variant

async def help_command(update, _):
    await update.message.reply_text("Используйте `/start` для тестирования.")


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('tab', tab))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(CommandHandler('help', help_command))

    app.run_polling()