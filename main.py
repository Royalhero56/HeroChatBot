from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters
from mongo_chat import detect_intent, get_reply, send_human_reply
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")


async def start(update, context):
    await update.message.reply_text("Hi! Human wala chat mode ON 😄")


async def chat(update, context):
    user_msg = update.message.text
    chat_id = update.effective_chat.id

    intent = detect_intent(user_msg)
    bot_reply = get_reply(intent)

    await send_human_reply(context, chat_id, bot_reply)


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("Human-like MongoDB bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()
