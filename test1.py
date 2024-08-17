from telethon import TelegramClient, events

api_id = 9731437
api_hash = '945bd735e9c66c5e126c5d73fc15ca1d'
bot_token = '6185899395:AAFJQbzaQiR-yHWx4zUriBX5uSOk73K52VE'



if __name__ == '__main__':
    client = TelegramClient("bot_session", api_id, api_hash)

    @client.on(events.NewMessage(pattern=r'\.(pdf|doc)$'))  # Accept PDF and DOC files only
    async def handle_file(event):
        file = await event.message.download_media()
        # Basic check for file extension (not processing content)
        if file.ext.lower() in ('.pdf', '.doc'):
            print(f"Received file: {file.name}")
            # Print type selection
            keyboard = [
                [events.InlineKeyboardButton(text='Black and White', callback_data='print_type_bw')],
                [events.InlineKeyboardButton(text='Color', callback_data='print_type_color')],
            ]
            await event.reply("Choose print type:", reply_markup=keyboard)
            @client.on(events.CallbackQuery)
            async def handle_callback(event):
                print(f"Callback received: {event.data.decode()}")
                if event.data.decode() == 'print_type_bw':
                    # User selected Black and White
                    await event.answer("Black and White printing selected.", show_alert=True)
                    # Page selection (All Pages only in this example)
                    keyboard = [events.InlineKeyboardButton(text='All Pages', callback_data='print_pages_all')]
                    await event.message.reply("Select pages to print:", reply_markup=keyboard)
                    @client.on(events.CallbackQuery)
                    async def handle_pages_callback(event):
                        if event.data.decode() == 'print_pages_all':
                            # User selected All Pages
                            await event.answer("All pages selected.", show_alert=True)
                            # Paper size selection
                            keyboard = [
                                [events.InlineKeyboardButton(text='A4', callback_data='paper_size_a4')],
                                [events.InlineKeyboardButton(text='A3', callback_data='paper_size_a3')],
                                [events.InlineKeyboardButton(text='A2', callback_data='paper_size_a2')],
                                [events.InlineKeyboardButton(text='Letter', callback_data='paper_size_letter')],
                            ]
                            await event.message.reply("Choose paper size:", reply_markup=keyboard)
                            @client.on(events.CallbackQuery)
                            async def handle_size_callback(event):
                                if event.data.decode() in (
                                    'paper_size_a4', 'paper_size_a3', 'paper_size_a2', 'paper_size_letter'
                                ):
                                    # User selected paper size
                                    paper_size = event.data.decode().split('_')[-1]
                                    await event.answer(f"{paper_size} paper size selected.", show_alert=True)
                                    # Summarize selection and provide further instructions (e.g., contact info)
                                    await event.message.reply(
                                        "Your print selection:\n"
                                        f"- Print type: Black and White\n"
                                        f"- Pages: All Pages\n"
                                        f"- Paper size: {paper_size}\n"
                                        "\nFor placing an order, please contact..."  # Add contact information
                                    )
                elif event.data.decode() == 'print_type_color':
                    # User selected Color (similar logic for other options)
                    await event.answer("Color printing selected.", show_alert=True)
                    # ...
                # Handle other callback data for different options
        else:
            await event.reply("Unsupported file")