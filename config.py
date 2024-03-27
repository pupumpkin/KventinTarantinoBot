import telebot

LOGS_PATH = "log_file.txt"
TOKEN = "token"
bot = telebot.TeleBot(TOKEN)

IAM_TOKEN = """IAM_TOKEN"""
HEADERS = {
            "Authorization": f"Bearer {IAM_TOKEN}",
            "Content-Type": "application/json"}
