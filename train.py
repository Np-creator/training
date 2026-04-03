from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters

TOKEN = "####"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your bot 🤖")

async def name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Hello")
    await update.message.reply_text("Your name is ...? ")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("yourname", name, filters=filters.Regex("(?i)^/yourname$")))

app.run_polling()