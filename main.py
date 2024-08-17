import os
import time
from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon.tl.custom import Button

sessionfile = 'D:\\telegrambot\\session'
filename = 'D:\\telegrambot\\downloads'

api_id = 9731437
api_hash = '945bd735e9c66c5e126c5d73fc15ca1d'
api_bot = '6185899395:AAFJQbzaQiR-yHWx4zUriBX5uSOk73K52VE'

phone = +919574531441
password = ''
download_folder = 'D:\\telegrambot\\downloads'

if __name__ == '__main__':
    # loading credentials
    client = TelegramClient(sessionfile, api_id, api_hash, sequential_updates=True)

    @client.on(events.NewMessage(incoming=True))
    async def handle_incoming_message(event):
        if event.is_private:

            if event.message.media:
                await event.download_media(file=os.path.join(download_folder, 'file1'))

                buttons = [
                    Button.inline("Option 1", b'1'),
                    Button.inline("Option 2", b'2'),
                ]

                # Create a reply markup with the buttons

                # Send a message with the options
                await event.respond("Here are some options:", buttons = buttons)



            if event.from_id is not None:
                from_ = await event.client.get_entity(event.from_id)

                if not from_.bot:
                    print(time.asctime(), '-', event.message)
                    time.sleep(1)
                    if 'hello' in event.raw_text:
                        await event.respond("Hello budyy.....")

    @client.on(events.NewMessage(outgoing=True))
    async def handle_outgoing_message(event):
        await event.respond.Button

print(time.asctime(), '-', 'Auto-Replying...')
client.start(phone, password)

client.run_until_disconnected()
print(time.asctime(), '-', 'Stopped!')