import matplotlib.pyplot as plt
import mplfinance as mpf
import threading
import time

class CryptoChart:
    def __init__(self, parent):
        self.parent = parent
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.parent)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update_chart(self, symbol):
        def fetch_data():
            while True:
                # Aqui você deve buscar os dados da criptomoeda em tempo real.
                # Atualize a figura e o canvas com os novos dados.
                time.sleep(60)  # Atualiza a cada 60 segundos

        threading.Thread(target=fetch_data).start()
