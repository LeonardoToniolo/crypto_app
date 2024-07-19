import requests


class BinanceAPIClient:
    BASE_URL = "https://api.binance.com"

    @staticmethod
    def get_all_cryptos():
        try:
            response = requests.get(
                f"{BinanceAPIClient.BASE_URL}/api/v3/ticker/price")
            response.raise_for_status(
            )  # Levanta um erro para respostas com status HTTP 4xx/5xx
            cryptos = response.json()
            if isinstance(cryptos, list):
                return cryptos
            else:
                print("Unexpected response format")
                return []
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from Binance API: {e}")
            return []

    @staticmethod
    def buy_crypto(symbol, quantity):
        # Aqui você deve implementar a lógica para comprar a cripto usando a API da Binance.
        # A API real requer autenticação e permissões adequadas.
        pass
