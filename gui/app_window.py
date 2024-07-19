import tkinter as tk
from tkinter import ttk
from binance_api.api_client import BinanceAPIClient
from gui.crypto_chart import CryptoChart


class CryptoApp:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Crypto Trading App")
        self.create_widgets()

    def create_widgets(self):
        self.crypto_list = ttk.Combobox(self.root)
        self.crypto_list.grid(row=0, column=0, padx=10, pady=10)

        self.buy_button = ttk.Button(self.root,
                                     text="Buy",
                                     command=self.buy_crypto)
        self.buy_button.grid(row=0, column=1, padx=10, pady=10)

        self.chart_frame = tk.Frame(self.root)
        self.chart_frame.grid(row=1, column=0, columnspan=2)

        self.crypto_chart = CryptoChart(self.chart_frame)
        self.load_cryptos()

    def load_cryptos(self):
        cryptos = BinanceAPIClient.get_all_cryptos()
        if cryptos:
            self.crypto_list['values'] = [
                crypto['symbol'] for crypto in cryptos
            ]
        else:
            self.crypto_list['values'] = []

    def buy_crypto(self):
        selected_crypto = self.crypto_list.get()
        quantity = 1  # Aqui você pode adicionar um campo para o usuário inserir a quantidade
        BinanceAPIClient.buy_crypto(selected_crypto, quantity)

    def run(self):
        self.root.mainloop()
