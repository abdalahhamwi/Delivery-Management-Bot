import django
import os
import sys
from asgiref.sync import sync_to_async

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from orders.models import Order


Bot_Token = "8559920620:AAFKAmyWtNkS_yY0cmet_CkfBTUjyKqFROc"
Bot_UserName = "@Django-Management-Orders"


@sync_to_async
def get_order_by_id(order_id: int) -> str:
    try:
        order = Order.objects.get(id=order_id)
        return (
            f"Order ID: {order.id}\n"
            f"Status: {order.get_status_display()}\n"
            f"Created: {order.created}\n"
            f"Adderss: {order.adderss}\n"
        )
    except Order.DoesNotExist:
        return f"Order with ID {order_id} does not exist!"



async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.from_user.username
    await update.message.reply_text(
        f"Hello, {username}! I am a Management Order Bot.\n"
        f"Please enter your Order ID to check its status."
    )


async def handle_order_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text.isdigit():
        order_id = int(text)
        response = await get_order_by_id(order_id)
    else:
        response = "Invalid input. Please send a valid numeric order ID."

    await update.message.reply_text(response)


if __name__ == '__main__':
    app = ApplicationBuilder().token(Bot_Token).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_order_query))

    app.run_polling(poll_interval=3)
