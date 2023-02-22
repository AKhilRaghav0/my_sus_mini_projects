import subprocess
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Telegram bot token
TOKEN = "BOT_TOKEN"

# Create the bot object
bot = telegram.Bot(token=TOKEN)

# Define a function to handle the "/start" command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! Send me a command and I'll execute it on the system.")

# Define a function to handle incoming messages
def execute_command(update, context):
    # Get the text of the incoming message
    command = update.message.text.strip()
    
    # Run the command using subprocess
    output = subprocess.check_output(command, shell=True, universal_newlines=True)

    # Send the output back to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=output)

# Create the Updater and add the handlers
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, execute_command))

# Start the bot
updater.start_polling()
updater.idle()

