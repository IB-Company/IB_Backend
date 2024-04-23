from fastapi import APIRouter

from service.exchange_rate_service import ExchangeRateService

router = APIRouter(prefix="/api/v1/exchange-rate", tags=["exchange_rate"])

exchange_rate_service = ExchangeRateService()


@router.get("/{concurrency_code}")
async def get_exchange_rate(concurrency_code: str):
    return exchange_rate_service.get_exchange_rate(concurrency_code)
