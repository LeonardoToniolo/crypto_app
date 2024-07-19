import requests

class BinanceAPIClient:
    BASE_URL = "https://api.binance.com"

    @staticmethod
    def get_all_cryptos():
        response = requests.get(f"{BinanceAPIClient.BASE_URL}/api/v3/ticker/price")
        return response.json()

    @staticmethod
    def buy_crypto(symbol, quantity):
        # Aqui você deve implementar a lógica para comprar a cripto usando a API da Binance.
        # A API real requer autenticação e permissões adequadas.
        pass
