import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "ZCU5K32SQ1I0G2CQ"
API_URL = "https://www.alphavantage.co/query"

class StockPriceFetcher:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Price Fetcher")
        self.root.geometry("350x200")

        tk.Label(root, text="Enter Stock Ticker:").pack(pady=5)
        self.ticker_entry = tk.Entry(root)
        self.ticker_entry.pack(pady=5)

        tk.Button(root, text="Get Price", command=self.get_stock_price).pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=10)

    def get_stock_price(self):
    
        ticker = self.ticker_entry.get().strip().upper()

        if not ticker:
            messagebox.showwarning("Input Error", "Please enter a stock ticker.")
            return

        try:
            params = {
                "function": "GLOBAL_QUOTE",
                "symbol": ticker,
                "apikey": API_KEY
            }
            response = requests.get(API_URL, params=params)
            response.raise_for_status() 

            data = response.json()

            print(data)

            if "Global Quote" not in data:
                raise KeyError("Invalid stock ticker or API issue.")

            stock_price = data["Global Quote"]["05. price"]
            self.result_label.config(text=f"{ticker} Price: ${stock_price}", fg="green")

        except requests.exceptions.ConnectionError:
            messagebox.showerror("Network Error", "No internet connection. Please check your network.")
        except KeyError:
            messagebox.showerror("API Error", "Invalid stock ticker or issue with API response.")
        except requests.exceptions.HTTPError as e:
            messagebox.showerror("HTTP Error", f"API Error: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    StockPriceFetcher(root)
    root.mainloop()
