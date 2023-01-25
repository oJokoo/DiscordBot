import discord
import responses
import requests
import shutil
import os
from io import BytesIO
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\jiths\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA2NzIwODkxMjY3NzM4NDMxMg.GyuBAI.C0bFTGH_smoMozOK63RX_QSEKfO5yMGo8cAULs'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.attachments:
            print(message.attachments)
            imageURL = message.attachments[0].url
            fileName = message.attachments[0].filename

            print(imageURL, fileName)

            res = requests.get(imageURL, stream=True)

            if res.status_code == 200:
                with open(fileName, 'wb') as f:
                    shutil.copyfileobj(res.raw, f)
                print('Image sucessfully Downloaded: ', fileName)
            else:
                print('Image Couldn\'t be retrieved')

            print(fileName)
            img = Image.open(fileName)
            text = tess.image_to_string(img)
            print(text)

            os.remove(fileName)  # Remove file photo after it has been processed with AI

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        # if user_message[0] == '?':
        #     user_message = user_message[1:]
        #     await send_message(message, user_message, is_private=True)
        # elif user_message[0] == '!':
        #     await send_message(message, user_message, is_private=False)
        # else:
        #     return

    client.run(TOKEN)
