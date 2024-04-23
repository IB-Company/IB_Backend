import requests
from db.redis import conn
import datetime


class ExchangeRateService:
    def __init__(self):
        self.redis_client = conn.con

    def get_exchange_rate(self, currency_code: str):
        exchange_rate = self.redis_client.get(currency_code)

        if exchange_rate:
            return {"exchange_rate": exchange_rate}

        response = requests.get(f'https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRW{currency_code}')
        response_to_json = response.json()

        get_exchange_rate = response_to_json[0]["basePrice"]

        self.redis_client.set(currency_code, get_exchange_rate, datetime.timedelta(minutes=5))

        return {"exchange_rate": get_exchange_rate}
