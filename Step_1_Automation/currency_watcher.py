import requests
import datetime

url = "https://open.er-api.com/v6/latest/USD"
response = requests.get(url)

data = response.json()
currencies = data["rates"]

with open("currency_log.txt", "a") as f:
    f.write(datetime.datetime.now().strftime("%d/%m/%Y\n\n"))
    for i in currencies:
        f.write(f"{i}: {currencies[i]}\n")
        f.write(f"1 {i} = {currencies["RUB"]/currencies[i]} RUB\n")
