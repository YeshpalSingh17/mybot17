from pyrogram import Client, filters


api_id=21588567
api_hash="78240039842b973f5139136864b6648f"
bot_token="6946044714:AAECjchZJkcvXmxcuYzcnI4yPvXtev2eX-o"
app = Client("yeshpal_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define a function to handle the /start command
@app.on_message(filters.command("start"))
def start_command(client, message):
    # Send "Hello" as a response to the /start command
    message.reply_text("Hello!")

# Run the bot
app.run()
