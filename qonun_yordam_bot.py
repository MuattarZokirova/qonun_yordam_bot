from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = '7881698949:AAEMr_wFyMbE0lDtP5PegK8QmDuqhkLHKiw'  # ← bu yerga o'zingizning bot tokeningizni qo'ying

# /start buyrug'iga javob
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    print(f"📨 Yangi foydalanuvchi: {user.full_name} (@{user.username}) - ID: {user.id}")

    await update.message.reply_text(
        "Assalomu alaykum! Men *Muattar Zokirova*.\n\n"
        "🇰🇷 *Koreyada yashayotgan chet elliklar uchun* qonuniy maslahat va tarjima xizmatlari ko‘rsataman.\n\n"
        "Quyidagi xizmatlardan birini tanlang:\n"
        "1️⃣ Viza olish va uzaytirish\n"
        "2️⃣ Advokat bilan maslahat\n"
        "3️⃣ Hujjatlar tayyorlash\n"
        "4️⃣ Konsultatsiyaga yozilish\n"
        "5️⃣ Tarjima xizmati\n\n"
        "⚠️ *Baʼzi xizmatlar pullik.* Narxlar oldindan aytiladi va sizga alohida xabar qilinadi.\n\n"
        "💳 *To‘lov uchun hisob:*\n"
        "*Muattar Zokirova*\n"
        "Toss Bank 토스뱅크\n"
        "`1001-2440-1345`",
        parse_mode="Markdown"
    )

# Oddiy matnli xabarlarga javob
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text
    print(f"\n📨 Xabar: {user.full_name} (@{user.username})\nID: {user.id}\n✉️: {text}\n")

    await update.message.reply_text("Xabaringiz qabul qilindi. Tez orada siz bilan bog‘lanamiz.")

# Botni ishga tushurish
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot ishga tushdi.")
    app.run_polling()

if __name__ == '__main__':
    main()
