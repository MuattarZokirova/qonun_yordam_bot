from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Bot tokeningizni shu yerga yozing
TOKEN = "7881698949:AAEMr_wFyMbE0lDtP5PegK8QmDuqhkLHKiw"

# Foydalanuvchi xabari kelganda chiqariladi
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat_id = update.effective_chat.id
    text = update.message.text

    print("\n📨 Yangi xabar!")
    print(f"👤 Ism: {user.full_name}")
    print(f"🔗 Username: @{user.username}" if user.username else "🔗 Username: yo‘q")
    print(f"🆔 Chat ID: {chat_id}")
    print(f"✉️ Xabar: {text}\n")

    await update.message.reply_text("Xabaringiz qabul qilindi ✅ Tez orada javob olasiz.")

# Admin javobi uchun /reply komandasi
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if len(args) < 2:
        await update.message.reply_text("❗ Foydalanish: /reply CHAT_ID xabar matni")
        return

    chat_id = int(args[0])
    message = " ".join(args[1:])

    try:
        await context.bot.send_message(chat_id=chat_id, text=message)
        await update.message.reply_text("✅ Javob yuborildi.")
    except Exception as e:
        await update.message.reply_text(f"❌ Xatolik: {e}")

# Botni ishga tushirish
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.add_handler(CommandHandler("reply", reply))
app.run_polling()
