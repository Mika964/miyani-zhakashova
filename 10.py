from telebot import types
TOKEN = "8212732183:AAGsmBdv6mWSF_xZYDhaexK_ojwrvMnbxk8"
bot = telebot.TeleBot(TOKEN)


# [вопрос, omвет1, ответ2, omвеm3, оmвеm4, правильный_omвет]
questions = [
    ["Сколько будет 2 + 2?", "3", "4", "5", "6", "14"],
    ["Столица Франции?", "Берлин", "Мадрид", "Рим", "Париж"],
    ["Какой язык используется в Telegram-ботах?", "Java", "Python", "C++", "PHP", "Python"]
]

user_question_index = () # chat_id -> индекс вопроса
user_score = ()          # chat_id -> баллы


def send_question (chat_id):
    index = user_question_index.get(chat_id, 0)  

    if index >= len(questions) :
        score = user_score.get(chat_id, 0)
        bot. send_message(
             chat_id,
            f" Bикторина оконччена!\n"
            f"Ваш результат: {score} из {len(questions)}"
        )
        return


    q = questions [index]


    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range (1, 5):
        keyboard. add (types.KeyboardButton(q[i]))


    keyboard.add(types.KeyboardButton("— Следующий вопрос"))


    bot. send_message(chat_id, f"? {q[0]}", reply_markup=keyboard)


@bot-message_handler (commands=["start"])
def start(message):
    chat_id = message.chat.id
    user_question_index[chat_id] = 0
    user_score [chat id] = 0
    send_question (chat_id)


@bot.message_handler(func=Lambda message: True)
def handle_answer (message) :
    chat_id = message.chat.id


    if chat_id not in user_question_index:
        return
    

    index = user_question_index[chat_id]


    if message. text == "- Следующий вопрос":
         user_question_index[chat_id] += 1
         send_question (chat_id)
         return

    if index >= len (questions):
        return
    
    correct_answer = questions [index][5]


    if message.text == correct_answer:
        user_score[chat_id] += 1
        bot. send_message(chat_id, "* Верно!")
    else:
        bot. send_message (
             chat_id,
           f" Неверно! Правильный ответ: {correct_answer}")
bot-polling()