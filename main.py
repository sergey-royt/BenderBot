import telebot
from json import load
from random import choice
from dotenv import load_dotenv
from os import getenv


load_dotenv()
bot = telebot.TeleBot(getenv('TELEGRAM_BOT_TOKEN'))
phrases = load(open('phrases.json'))
phrase_count = len(phrases)


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(
        message.chat.id,
        'Это чат-бот имитирующий робота Бендера из Футурамы. Что бы начать просто отправь мне сообщение')

@bot.message_handler(content_types=['text'])
def reply(message):
    bot.send_message(message.chat.id, choose_phrase(message))


def choose_phrase(message):
    for w in message.text.lower().split():
        for phrase in phrases:
            for word in phrase.lower().split():
                if w in word:
                    return phrase
    return choice(phrases)


bot.polling()
