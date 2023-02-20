import telebot
from Parser import *

token = '6125693388:AAFoeusnkSNA63KIy0VshbSM1zmskeEn1tQ'
bot = telebot.TeleBot(token)
urlNew = "https://petition.president.gov.ua/?status=active&sort=date&order=desc"
urlTop = "https://petition.president.gov.ua/?status=active&sort=votes&order=desc"
@bot.message_handler(commands=['go'])
def hello(message):
    bot.send_message(message.chat.id, "Щоб запарсити сайт, введіть цифру:")
    bot.send_message(message.chat.id, "1 - нові петиції, 2 - найпопулярніші петиції")
@bot.message_handler(content_types=['text'])
def newest(message):
    if message.text.lower() in "1":
        newText = parseTitle(urlNew)
        newUrls = parseUrl(urlNew)
        toSend = str()
        for i in range(len(newText)//2):
            toSend += newText[0] + " "
            toSend += "https://petition.president.gov.ua" + newUrls[0] + "\n"
            del newText[0]
            del newUrls[0]
        bot.send_message(message.chat.id, toSend)
        toSend = str()
        for i in range(len(newText)):
            toSend += newText[0] + " "
            toSend += "https://petition.president.gov.ua" + newUrls[0] + "\n"
            del newText[0]
            del newUrls[0]
        bot.send_message(message.chat.id, toSend)
    elif message.text.lower() in "2":
        newText = parseTitle(urlTop)
        newUrls = parseUrl(urlTop)
        toSend = str()
        for i in range(len(newText)//2):
            toSend += newText[0] + " "
            toSend += "https://petition.president.gov.ua" + newUrls[0] + "\n"
            del newText[0]
            del newUrls[0]
        bot.send_message(message.chat.id, toSend)
        toSend = str()
        for i in range(len(newText)):
            toSend += newText[0] + " "
            toSend += "https://petition.president.gov.ua" + newUrls[0] + "\n"
            del newText[0]
            del newUrls[0]
        bot.send_message(message.chat.id, toSend)
    else:
        bot.send_message(message.chat.id, "Обери цифру або 1, або 2, баран")
bot.polling()