from environs import Env
import environs
import telebot
from pycoingecko import CoinGeckoAPI
from telebot import TeleBot

env = environs.Env()
env.read_env(".env")

BOT_TOKEN = "5535695768:AAE4RQuM5ReWF6BeKRi4u5S7p63XNxLhnyU"

# Crypto API - coin gecko
# Telegram API - telebot
# Imprimir valores
bot = TeleBot(token=BOT_TOKEN)
coin_client = CoinGeckoAPI()

# print(coin_client.get_price(ids="bitcoin", vs_currencies="brl")["bitcoin"]["brl"])


@bot.message_handler(content_types=["text"])
def crypto_price_message_handler(message):
    crypto_id = message.text
    price_response = coin_client.get_price(ids=crypto_id, vs_currencies="brl")

    if price_response:
        price = price_response[crypto_id]["brl"]
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Atualmente preço do {crypto_id} está: R${price}",
        )
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Olá! Para saber o preço atual de alguma criptomoeda digite o nome dela! Ex: bitcoin (Para preço atual do Bitcoin) , ethereum (Para preço atual do Ethereum)",
        )


if __name__ == "__main__":
    bot.polling()
