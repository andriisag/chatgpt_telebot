import telebot
import openai

openai.api_key = ""
bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def start_message(message):
     bot.send_message(message.chat.id, text="Hello, " + message.chat.first_name)
@bot.message_handler(content_types=['text'])
def message(message):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "user", "content": f"{message.text}"}
    ]
    )
    bot.send_message(message.chat.id, str(completion.choices[0].message.content))

bot.infinity_polling()
