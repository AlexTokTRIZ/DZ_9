from tok import*
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Application,CommandHandler,ContextTypes,ConversationHandler,MessageHandler,filters
import logging

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

CHOOSING_GOOD, CHOOSING_BAD,TRICK,TYPING_REPLY, TYPING_CHOICE = range(5)

reply_keyboard = [["01 Длина"],["02 Ширина"],["02 Ширина"],["03 Ширина"],["04 Ширина"],["05 Ширина"],["06 Ширина"],["07 Ширина"],["Done"],]
end_keyboard = [["Ещё","Конец"],]
markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
markup_end = ReplyKeyboardMarkup(end_keyboard, resize_keyboard=True, one_time_keyboard=True)
good,bad = range(2)
def facts_to_str(user_data: dict[str, str]) -> str:
    """Вспомогательная функция для форматирования
    собранной информации о пользователе."""
    facts = [f"{key} - {value}" for key, value in user_data.items()]
    return "\n".join(facts).join(["\n", "\n"])

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message, text="Привет", reply_markup=reply_markup)
#     return reply_markup

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Начvало разговора, просьба ввести данные."""
    user_id = update.message.from_user.id
    print(user_id)
    await update.message.reply_text("Выберите, что хотите улучшить:",reply_markup=markup)
    return CHOOSING_GOOD

async def regular_choice_good(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Запрос информации о выбранном предопределенном выборе."""
    text = update.message.text
    context.user_data["choice"] = text
    good=text
    print(good)
    #await update.message.reply_text(f"Your {text.lower()}? Yes, I would love to hear about that!")
    await update.message.reply_text("Выберите, что ухудшается:",reply_markup=markup)
    return CHOOSING_BAD

async def regular_choice_bad(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Запрос информации о выбранном предопределенном выборе."""
    text = update.message.text
    context.user_data["choice"] = text
    bad=text
    print(bad)
    await update.message.reply_text('Вам рекомендуются следующие приёмы',reply_markup=markup_end)
    # query = update.callback_query
    # query.answer()
    # query.edit_message_text(text="Вам рекомендуются следующие приёмы")
    return TRICK

async def custom_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Запрос описания пользовательской категории."""
    await update.message.reply_text(
        'Alright, please send me the category first, for example "Most impressive skill"'
    )
    return TYPING_CHOICE

async def received_information(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Store info provided by user and ask for the next category."""
    user_data = context.user_data
    text = update.message.text
    category = user_data["choice"]
    user_data[category] = text
    del user_data["choice"]

    await update.message.reply_text(
        "Вам рекомендуются следующие приёмы"
        f"{facts_to_str(user_data)}You can tell me more, or change your opinion", reply_markup=markup)
    return CHOOSING

async def done(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Вывод собранной информации и завершение разговора."""
    user_data = context.user_data
    if "choice" in user_data:
        del user_data["choice"]

    await update.message.reply_text("До новых встреч!", reply_markup=ReplyKeyboardRemove(),)
    user_data.clear()
    return ConversationHandler.END


if __name__ == "__main__":
    application = Application.builder().token(tok()).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSING_GOOD: [MessageHandler(
                filters.Regex("^(01 Длина|02 Ширина|Number of siblings)$"), regular_choice_good),],
            CHOOSING_BAD: [MessageHandler(
                filters.Regex("^(01 Длина|02 Ширина|Number of siblings)$"), regular_choice_bad),
                MessageHandler(filters.Regex("^Something else...$"), custom_choice), ],

            TRICK: [MessageHandler(filters.Regex("^Ещё$"), start),
                    MessageHandler(filters.Regex("^Конец$"), done),],

            TYPING_CHOICE: [
                MessageHandler(
                    filters.TEXT & ~(filters.COMMAND | filters.Regex("^Done$")), regular_choice_bad
                )
            ],
            TYPING_REPLY: [
                MessageHandler(
                    filters.TEXT & ~(filters.COMMAND | filters.Regex("^Done$")),
                    received_information,
                )
            ],
        },
        fallbacks=[MessageHandler(filters.Regex("^Done$"), done)],
    )

    application.add_handler(conv_handler)
    # Запуск бота.
    application.run_polling()