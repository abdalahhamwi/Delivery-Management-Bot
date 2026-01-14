import django
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from typing import Final
from telegram import update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from orders.models import Order
Bot_Token = "8559920620:AAFKAmyWtNkS_yY0cmet_CkfBTUjyKqFROc"
