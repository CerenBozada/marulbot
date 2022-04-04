from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import re
import telegram
my_token = 'replace with token here'
# bot = telegram.Bot(token=token)


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.


def start(update, context):
    """Send a message when the command /start is issued."""
    print(update.message)
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""

    message = update.message.text.lower()
    if "uyan" in message.lower():
        message = update.message.text

        hourRegex = r'\b(([01]?[0-9]|2[0-3])([:.][0-5][0-9]))\b'
        print(re.findall(hourRegex, message))
        hour = re.findall(hourRegex, message)[0][0]
        dayRegex = r'(\bbugün|yarın|pazartesi|salı|çarşamba|perşembe|cuma|cumartesi|pazar\b)'
        print(re.findall(dayRegex, message))
        day = re.findall(dayRegex, message)[0]
        # args = message.split(" ")[1:]

        update.message.reply_text(
            f"tamam  {day} {hour} da  uyandıracağım ")

    elif "loto oyna" in message:
        import random
        randomlist = " ".join(str(x) for x in random.sample(range(1, 60), 6))
        update.message.reply_text(f"Şanslı numaralar! {randomlist} ")
    elif "günaydın" in message:
        update.message.reply_text("Günaydın")
    elif "napıyosun" in message or "naber" in message:
        update.message.reply_text("iyi sendenn")

    elif "adın ne" in message or "kimsin" in message:
        update.message.reply_text("🥬marul")

    else:
        update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(my_token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("alarmkur", pass_args=True))
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
