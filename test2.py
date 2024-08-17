from telethon.sync import TelegramClient, events
from telethon import functions, types

api_id = 9731437
api_hash = '945bd735e9c66c5e126c5d73fc15ca1d'
bot_token = '6185899395:AAFJQbzaQiR-yHWx4zUriBX5uSOk73K52VE'
# Initialize the Telegram client
client = TelegramClient('bot_session', api_id, api_hash)


@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Welcome to the printing bot! Please send the document you want to print.')


@client.on(events.NewMessage)
async def handle_message(event):
    if event.document:
        await handle_document(event)


async def handle_document(event):
    document = event.message.file
    file_name = document.name
    await event.respond(f"Document received: {file_name}")

    # Save the file locally
    file_path = f'./{file_name}'
    await client.download_media(document, file_path)

    # Ask questions
    await ask_print_type(event)


async def ask_print_type(event):
    await event.respond(
        'Choose type of print:',
        buttons=[
            types.KeyboardButton('Black and White'),
            types.KeyboardButton('Color')
        ]
    )
    # Register the next handler
    client.register_next_step_handler(event, ask_pages)


async def ask_pages(event):
    response = event.message.text
    await event.respond(f'You chose: {response}')

    await event.respond(
        'Pages you want to print:',
        buttons=[
            types.KeyboardButton('All Pages'),
            types.KeyboardButton('Custom')
        ]
    )
    # Register the next handler
    client.register_next_step_handler(event, ask_paper_type)


async def ask_paper_type(event):
    response = event.message.text
    await event.respond(f'You chose: {response}')

    await event.respond(
        'Choose the type of prints:',
        buttons=[
            types.KeyboardButton('A4'),
            types.KeyboardButton('A3'),
            types.KeyboardButton('A2'),
            types.KeyboardButton('Letter')
        ]
    )
    # Register the next handler
    client.register_next_step_handler(event, finalize_print)


async def finalize_print(event):
    response = event.message.text
    await event.respond(f'You chose: {response}')

    await event.respond('Your print request has been finalized. Thank you!')

    # Save responses to a file (you can modify this as needed)
    with open('print_requests.txt', 'a') as file:
        file.write(f"Print type: {event.message.text}\n")
        file.write(f"Pages: {event.message.text}\n")
        file.write(f"Paper type: {event.message.text}\n")
        file.write('\n')


async def main():
    await client.start()
    await client.run_until_disconnected()


if __name__ == '__main__':
    client.loop.run_until_complete(main())
