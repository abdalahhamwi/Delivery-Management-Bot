# 📦 Delivery Management Telegram Bot 

A **Django‑powered Telegram Bot** that allows users to check the status of their delivery orders by sending the order ID through Telegram.

This project demonstrates backend integration between **Django**, **Telegram Bot API**, and async/sync bridging.



## 🚀 Features

**Check order status** by sending an order ID  
**Telegram Bot integration** using `python-telegram-bot`  
**Async + Sync bridging** using `sync_to_async`  
**Django ORM** for database queries  
Clean and modular architecture  
Easy to extend for real delivery systems  



## 🛠️ Tech Stack

| Technology              | Purpose                     |
|------------------------|-----------------------------|
| **Python 3.12**        | Main language               |
| **Django**             | Backend framework & ORM     |
| **Telegram Bot API**   | User interaction            |
| **python-telegram-bot**| Bot framework               |
| **SQLite/PostgreSQL**  | Database                    |
| **asyncio + asgiref**  | Async execution             |



##  Installation & Setup

1. Install Project Dependencies
```bash
 pip install -r requirements.txt 
```

2. Apply Database Migrations
 ```bash
python manage.py migrate
```

3. Create Superuser (Required)
```bash
python manage.py createsuperuser
```

4. Run the Django Server
```bash
python manage.py runserver
```

5 . Add Sample Orders to the Database
After running the server, open the admin panel:
```bash
http://127.0.0.1:8000/admin/
```
Log in using the superuser you created.

Then add some Orders manually, for example:

Order ID: 1 — Status: Delivered

Order ID: 2 — Status: Pending

These orders will be used by the Telegram bot.

## 🤖 Run the Telegram Bot
Open a second terminal:
```bash
python bot.py
```
The bot is now online.

Open Telegram

Search for your bot

Press /Start
