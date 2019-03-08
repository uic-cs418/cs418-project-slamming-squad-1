from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
import sys
import csv
import matplotlib.pyplot as plt


class ScreenshotWebsite:
    def __init__(self):
        _start = time.time()
        options = Options()
        # options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox')  # # Bypass OS security model
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(options=options, executable_path='/usr/local/bin/chromedriver')
        # driver.get('http://coin360.com')
        driver.get('https://coin360.com/?period=[1546978000000,1552075600000]')
        driver.save_screenshot('screenshot-headless.png')
        driver.quit()
        _end = time.time()
        print('Total time processing {}'.format(_end - _start))


class ShowPriceGraph:
    def __init__(self):
        self.list_of_coins = ["bitcoin", "ethereum", "ripple", "litecoin", "eos",
                              "bitcoin cash", "tether", "binance coin", "stellar", "tron"]
        self.colors = ['red', 'green', 'cyan', 'magenta', 'yellow', 'orange', 'black', 'blue', 'lightgreen', 'purple']
        self.coin_data = []

        for coinname in self.list_of_coins:
            self.coin_data.append(self.open_csv("{}-24h.csv".format(coinname)))
        self.show_graph()
        self.show_graph_normalized()

    def open_csv(self, filename):
        firstrow = True
        times, prices = [], []
        with open(filename, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if firstrow:
                    firstrow = False
                else:
                    times.append(row[0][:10])
                    prices.append(float(row[1]))
        return [times, prices]

    def show_graph(self):
        fig, ax = plt.subplots(figsize=(7, 5))

        ax.set_title("Top 10 Cryptocurrency Price History")

        for i, data in enumerate(self.coin_data):
            times = [datetime.datetime.strptime(d, '%Y-%m-%d').date() for d in data[0]]
            ax.plot(times, data[1], color=self.colors[i], label=self.list_of_coins[i])

        plt.gcf().autofmt_xdate()
        plt.ylabel("Price")
        plt.legend()
        plt.grid()
        plt.show()
        fig.savefig('Top10_Cryptocurrency_Price_History.png', dpi=300)

    def show_graph_normalized(self):
        fig, ax = plt.subplots(figsize=(7, 5))

        ax.set_title("Top 10 Cryptocurrency Price History Normalized")

        for i, data in enumerate(self.coin_data):
            times = [datetime.datetime.strptime(d, '%Y-%m-%d').date() for d in data[0]]
            prices = []
            price_min = min(data[1])
            price_max = max(data[1])
            for price in data[1]:
                if price_max != price_min:
                    prices.append((price-price_min)/(price_max-price_min))
                else:
                    prices.append(0)
            ax.plot(times, prices, color=self.colors[i], label=self.list_of_coins[i])

        plt.gcf().autofmt_xdate()
        plt.ylabel("Price")
        plt.legend()
        plt.grid()
        plt.show()
        fig.savefig('Top10_Cryptocurrency_Price_History_Normalized.png', dpi=300)


def main():
    ShowPriceGraph()


if __name__ == '__main__':
    main()