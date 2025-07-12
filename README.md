

### 📄 `README.md`

markdown
# 🎥 Telegram IPTV Recording Bot

This is a professional-grade Telegram bot for recording IPTV streams using **FFmpeg** and controlling everything via **Telegram commands**.

---

## 🚀 Features

- ✅ IPTV recording using FFmpeg
- ✅ Telegram bot + userbot (admin access)
- ✅ Playback-friendly video upload
- ✅ Auto-captioning with time, size, duration
- ✅ Indian timezone (IST) support
- ✅ Forwarding to log/store channels
- ✅ Admin-only userbot with temp access control
- ✅ PHP stream (.m3u8) extractor support
- ✅ Modular structure (Pyrogram, Flask, Telebot)

---

## 📲 Termux Installation Guide

Follow these steps carefully to run the bot in **Termux (Android)**:

### 1. Install Required Termux Packages

```bash
pkg update -y && pkg upgrade -y   
````

### 2. install pkg

```bash

pkg install -y python clang ffmpeg git wget zip unzip libffi
```

### 3. Clone This Repository

```bash
git clone https://github.com/krishnanamdev1/iptv-recording-bot.git
cd iptv-recording-bot
```

### 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Python Dependencies (`requirements.txt`)

This project uses the following libraries:

```txt
pyrogram
tgcrypto
ffmpeg-python
python-dotenv
apscheduler
pytz
requests
pyTelegramBotAPI
python-telegram-bot
telethon
aiofiles
aiohttp
```

---

## 🔑 Environment Variables

Edit  `.env` file with the following variables:

```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
LOG_CHANNEL_ID=-100XXXXXXXXXX
STORE_CHANNEL_ID=-100XXXXXXXXXX
ADMIN_ID=123456456
```

> 💡 Get `API_ID` and `API_HASH` from [https://my.telegram.org](https://my.telegram.org)

---

## 🏁 Run the Bot

```bash
# Run normally
python main.py
```


## 🤝 Contributing

Pull requests are welcome. Please open an issue first to discuss major changes.

---

## 📜 License

This project is licensed under the MIT License.

```

