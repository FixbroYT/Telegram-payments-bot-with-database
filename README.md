
---


# 🚀 Telegram Payments Bot with Database  

This bot allows you to accept payments via **Stripe** and store user data in a database. Built using **Aiogram + SQLAlchemy**, it ensures seamless integration with Telegram and secure payment processing.

## 📌 Features  
✅ Accept payments via **Stripe Checkout**  
✅ Store users and payment statuses in **SQLite/PostgreSQL**  
✅ Automatically confirm payments and send success messages  
✅ Shortened payment links for better readability  
✅ Secure webhook handling with **ngrok**  

---

## 🛠 Tech Stack  
- **Python** (Aiogram, SQLAlchemy)  
- **Stripe API** (Checkout)  
- **Database** (SQLite / PostgreSQL)  
- **Ngrok** (For webhook testing)  

---

## 🚀 How to Set Up  

### 1️⃣ Install Dependencies  
First, clone the repository and install required packages:  
```bash
git clone https://github.com/yourusername/Telegram-payments-bot-with-database.git
cd Telegram-payments-bot-with-database
pip install -r requirements.txt
```

---

### 2️⃣ Set Up Your Environment Variables  
Create a `.env` file in the root directory and add your credentials:  
```ini
BOT_TOKEN=your_telegram_bot_token
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_PUBLIC_KEY=your_stripe_public_key
DATABASE_URL=sqlite+aiosqlite:///db.sqlite3
WEBHOOK_URL=https://your-ngrok-url/webhook
```

🔹 **BOT_TOKEN** – Get it from [@BotFather](https://t.me/BotFather)  
🔹 **STRIPE_SECRET_KEY & STRIPE_PUBLIC_KEY** – Get them from your [Stripe Dashboard](https://dashboard.stripe.com/)  
🔹 **DATABASE_URL** – Use SQLite (default) or configure PostgreSQL  
🔹 **WEBHOOK_URL** – Will be set up with ngrok  

---

### 3️⃣ Set Up Database  
Run the following command to initialize your database:  
```bash
python -m app.database.models
```
This will create necessary tables in **SQLite/PostgreSQL**.

---

### 4️⃣ Start Ngrok for Webhook  
Since Stripe requires a **public URL**, use `ngrok` to expose your local server:  
```bash
ngrok http 8000
```
Copy the **HTTPS URL** from ngrok and update `WEBHOOK_URL` in your `.env` file.

---

### 5️⃣ Run the Bot  
Start your bot with:  
```bash
python run.py
```
The bot will now listen for payments and process transactions.

---

## 💡 Usage  
1️⃣ A user sends the `/buy` command.  
2️⃣ The bot generates a **payment link** and sends it.  
3️⃣ The user completes payment via **Stripe Checkout**.  
4️⃣ Stripe sends a **webhook** confirming the payment.  
5️⃣ The bot sends a **confirmation message** and records the transaction.  

---

## 🎯 Future Improvements  
🔹 Add support for **multiple payment methods**  
🔹 Implement a **user dashboard** to track payments  
🔹 Support **subscription-based payments**  

---

## 📩 Contact  
If you have any issues or suggestions, feel free to open an **issue** or contact me directly. 😎  
```

---

Этот `README.md` даёт полную инструкцию по установке, настройке и запуску твоего бота с базой данных и оплатами через Stripe. 🚀
