import requests
import json

# Функция для получения курсов валют с API
def get_exchange_rates():
    url = "https://api.exchangeratesapi.io/latest"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data["rates"]
    else:
        print("Error: Unable to fetch exchange rates.")
        return None

# Функция для конвертации валют
def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency != "EUR":
        amount = amount / exchange_rates[from_currency]
    return amount * exchange_rates[to_currency]

# Основной код
if __name__ == "__main__":
    # Получение курсов валют
    exchange_rates = get_exchange_rates()
    if exchange_rates:
        # Ввод данных пользователем
        amount = float(input("Enter the amount: "))
        from_currency = input("Enter the base currency (e.g., USD): ").upper()
        to_currency = input("Enter the target currency (e.g., EUR): ").upper()

        # Конвертация валюты и вывод результата
        result = convert_currency(amount, from_currency, to_currency, exchange_rates)
        print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")
        input()
