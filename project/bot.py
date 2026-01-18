import django
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from typing import Final
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

def get_order_by_id(order_id: int) -> str:
    try:
        order = Order.objects.get(id=order_id) 
        return (
        f"order ID:(order.id)\n",
        f"status: (order.get_status_display())\n", 
        f"created : (order.created)\n",
        f"adderss : (order.adderss)\n",
        )
    except Order.DoseNotExist:
        return f"order with id (order.id) dose not exist" 
    
    
async def start_command(update: Update, contexts=ContextTypes.DEFAULT_TYPE):
    username = update.message.from_user.username
    await update.message.reply_text(f"Hello {username}! Iam A Management Order Bot. \nPlease Enter Your Order ID to Check its status.")
    
    
async def handle_order_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text.strip()
        if text.isdigit():
            order_id = int(text)
            response = await get_order_by_id(order_id)
        else:
            response = "Invalid input. please send a valid numeric order ID."
            await update.message.reply_text(response)
            
            
if __name__ == "__main__":
   app = ApplicationBuilder().token(Bot_Token).build()
   app.add_handler(CommandHandler("star", start_command))
   app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_order_query))