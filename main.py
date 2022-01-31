import telebot
import requests
from requests.structures import CaseInsensitiveDict


bot = telebot.TeleBot("5133225747:AAHys5_MWWJLaiLc-UxVvWVhpWEZmkEIXDo")

def link_change(m):
    caption = m.text

    url = "https://diskuploader.mypowerdisk.com/v1/tp/cp"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    caption_list = caption.split()

    newLink = []
    for caption_mdisk in caption_list:
        if 'https://mdisk.me/' in caption_mdisk:
            data = {"token": "33Ks8vOux6B4c4srrUK1","link": f"{caption_mdisk}"}
            # print(data)
            resp = requests.post(url, headers=headers, json=data)
            your_link = resp.text[14:-2]
            your_link = resp.text[14:-2]
            print(your_link)
            newLink.append(your_link)
            
    return ('\n').join(newLink)


@bot.message_handler(func=lambda message: True, content_types=['audio', 'video', 'document', 'text', 'location', 'contact', 'sticker'])
def default_command(message):
    text = link_change(message)
    bot.send_message(message.chat.id, text)

bot.infinity_polling()
