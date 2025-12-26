# Inline Maker Telegram Bot

A production-ready Telegram bot that publishes **image posts with captions and inline buttons**
directly to any channel **without forward tags**.

Designed for creators and admins who manage multiple Telegram channels and need a fast,
clean, and repeatable posting workflow.

---

## Overview

Inline Maker Bot allows the owner to create rich Telegram channel posts by interacting
with the bot in private chat.  
Each post is created dynamically and can be published to **any channel where the bot
has admin rights**.

The bot is optimized for **Docker and Render hosting** and follows best practices
for security and deployment.

---

## Key Features

- Image + caption posting
- Inline button with custom text and URL
- Dynamic channel selection per post
- No forward tag (direct posting)
- Owner-restricted access
- Docker-ready for cloud deployment
- Environment variable based configuration
- High performance using tgcrypto

---

## Workflow

1. Send a photo with caption to the bot (private chat)
2. Bot requests:
   - Button text
   - Button URL
   - Target channel ID or @username
3. Bot publishes the post directly to the specified channel

---

## Project Structure
inlineBot/ ├── inlineBot.py ├── requirements.txt └── Dockerfile
---

## Requirements

- Python 3.9 or higher
- Telegram Bot Token
- Telegram API ID & API Hash
- Docker (for hosting)

---

## Environment Variables

The following environment variables must be set on the hosting platform:

| Variable   | Description |
|-----------|-------------|
| API_ID    | Telegram API ID |
| API_HASH  | Telegram API Hash |
| BOT_TOKEN | Telegram Bot Token |
| OWNER_ID  | Telegram User ID of the bot owner |

> Sensitive credentials must **never** be hard-coded.

---

## Installation (Local)

```bash
pip install -r requirements.txt
python inlineBot.py

Deployment (Render / Docker)
Push the repository to GitHub
Create a new Web Service on Render
Select Docker as the runtime
Add environment variables
Deploy
The service will start automatically using the Dockerfile.
Security Notes
Do not commit .session files
Do not expose API credentials in source code
Always use environment variables for secrets
Use Cases
Anime & movie channels
File distribution channels
Content update channels
Multi-channel management
Professional Telegram publishing workflows

Author
Gurmeet Singh
Telegram Bot Developer

#License
This project is intended for personal and educational use.
You are free to modify and extend it for your own workflows.

#Support
If this project helps you, consider starring the repository or contributing improvements.
---

## ✅ Ye README kis level ka hai?
✔ Corporate / production style  
✔ Clean & minimal  
✔ Hosting-ready  
✔ GitHub showcase friendly

