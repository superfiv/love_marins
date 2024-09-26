python
import telebot
from telebot import types


API_TOKEN = '6928752413:AAFzrOPgjAUO7juJ4jdb5WHRJ8fOD1a2uxQ'
bot = telebot.TeleBot(API_TOKEN)


user_clicks = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Нажимай на кнопку, чтобы увеличить счетчик!")
    send_inline_keyboard(message.chat.id)

def send_inline_keyboard(chat_id):
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Кликни меня!", callback_data='click')
    keyboard.add(button)
    bot.send_message(chat_id, "👍 Нажми на кнопку!", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'click')
def handle_click(call):
    user_id = call.from_user.id
    if user_id not in user_clicks:
        user_clicks[user_id] = 0

    user_clicks[user_id] += 1
    bot.answer_callback_query(call.id, text="Вы кликнули!")
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text=f"Вы кликнули {user_clicks[user_id]} раз(а).",
                          reply_markup=call.message.reply_markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)