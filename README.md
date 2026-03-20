# Trading Bot Documentation

## Overview
This trading bot is designed to automate trading on various markets via Telegram. It leverages advanced algorithms to analyze market trends and execute trades based on predefined strategies.

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/ZeB522/trading-bot-telegram.git
   cd trading-bot-telegram
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment variables**:
   Make sure to set the following environment variables:
   - `TELEGRAM_API_KEY`: Your Telegram Bot API key.
   - `TRADE_API_KEY`: Your trading platform API key.

## Configuration
The configuration can be done via the `config.json` file located in the root directory. Here is an example of the configuration file:
```json
{
  "strategy": "default",
  "stake_amount": 100,
  "trading_pairs": ["BTC/USD", "ETH/USD"],
  "telegram_chat_id": "YOUR_CHAT_ID"
}
```

## Usage
To run the bot:
```bash
python bot.py
```
Once the bot is running, it will start listening for commands via Telegram. You can use commands like `/start`, `/status`, and `/trade <pair>` to interact with the bot.

## Contributing
If you'd like to contribute, please fork the repository and submit a pull request. For any issues, feel free to open an issue on GitHub.