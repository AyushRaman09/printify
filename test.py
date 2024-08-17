from telethon.sync import TelegramClient, events
from telethon.tl.custom import Button
import os
import time
from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon.tl.custom import Button

# Replace these values with your own API ID, API hash, and bot token
api_id = 9731437
api_hash = '945bd735e9c66c5e126c5d73fc15ca1d'
bot_token = '6185899395:AAFJQbzaQiR-yHWx4zUriBX5uSOk73K52VE'

sessionfile = 'D:\\telegrambot\\session'
filename = 'D:\\telegrambot\\downloads'

# Dictionary to store user choices
user_choices = {}

if __name__ == '__main__':
    client = TelegramClient("bot_session", api_id, api_hash)

    @client.on(events.NewMessage(incoming=True))
    async def incoming_message_handler(event):
        global user_choices

        if event.message.media and event.message.document:
            file_name = event.message.document.attributes[0].file_name
            await event.respond(f"Received document: {file_name}")

            buttons = [
                [Button.inline("Black and White Print", b"bw")],
                [Button.inline("Color Print", b"col")],
            ]
            message = await event.respond("Choose the type of print:", buttons=buttons)

            # Store the user ID along with the message ID to identify responses
            user_id = event.sender_id
            message_id = message.id
            user_choices[(user_id, message_id)] = None

    @client.on(events.CallbackQuery)
    async def callback_handler(event):
        global user_choices

        user_id = event.sender_id
        choice = event.data.decode("utf-8")

        # Check if the message corresponds to a button press initiated by the bot
        if (user_id) in user_choices:
            # Update the user's choice in the dictionary
            user_choices[(user_id)] = choice
            print(user_choices)

            await event.edit(f"You chose {choice}")
            # You can now use user_choices[(user_id, message_id)] to get the selected option

print("Listening for incoming messages...")
client.start(bot_token=bot_token)

client.run_until_disconnected()
print(time.asctime(), '-', 'Stopped!')


                    # buttons = [
                    #     [Button.inline("All Pages", b"ap")],
                    #     [Button.inline("Custom Pages", b"cp")],
                    # ]   
                    # await event.respond("Pages you want to print :", buttons=buttons)


                    # buttons = [
                    #     [Button.inline("A3", b"A3")],
                    #     [Button.inline("A4", b"A4")],
                    #     [Button.inline("Letter", b"letter")],
                    # ]   
                    # await event.respond("Choose the type of print:", buttons=buttons)