import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, CommandHandler, filters

TOKEN = "YOUR_BOT_TOKEN_HERE"  # Bu yerga o'zingizning bot tokeningizni kiriting

# Logging sozlamalari
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Global set to track user chat IDs
user_ids = set()

# Har bir yangi xabarni qabul qilish
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = update.message.text
    user_info = f"\n📨 Yangi xabar!\n👤 Ism: {user.full_name}\n🔗 Username: @{user.username}\n🆔 Chat ID: {user.id}\n✉️ Xabar: {message}"

    print(user_info)
    user_ids.add(user.id)

    # Istalgan javob
    await update.message.reply_text("Xabaringiz qabul qilindi!")

# Reply funksiyasi
async def reply_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("Foydalanish: /reply [chat_id] [xabar]")
        return

    chat_id = int(context.args[0])
    reply_text = " ".join(context.args[1:])
    try:
        await context.bot.send_message(chat_id=chat_id, text=reply_text)
        await update.message.reply_text("Xabar yuborildi!")
    except Exception as e:
        await update.message.reply_text(f"Xato yuz berdi: {e}")

# Asosiy funksiyani yaratish
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CommandHandler("reply", reply_command))

    print("🤖 Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
