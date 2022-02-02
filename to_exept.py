import requests
import json
from config import keys


class ConvertionExeption(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionExeption('Нельзя конвертировать одинаковую валюту!')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f'Убедитесь, что верно указали валюту "{quote}"')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'Убедитесь, что верно указали валюту "{base}"')

        try:
            amount = float(amount)
            if amount <= 0:
                raise ConvertionExeption('Невозможно выполнить запрос.')
        except ValueError:
            raise ConvertionExeption(f'Убедитесь, что верно указали количество "{amount}"')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base * amount
