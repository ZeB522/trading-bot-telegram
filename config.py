import os

class Config:
    API_TOKEN = os.getenv('API_TOKEN')
    BOT_NAME = os.getenv('BOT_NAME')
    CHAT_ID = os.getenv('CHAT_ID')
    # Additional configuration variables can be added here
