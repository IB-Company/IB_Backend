from fastapi import APIRouter

from service.weather.weather_model import WeatherResponse
from service.weather.weather_service import WeatherService

weather_controller = APIRouter(prefix="/api/v1/weather", tags=["weather"])
weather_service = WeatherService()


@weather_controller.get("/", description="위도&경도 => 그 지역의 날씨 정보")
async def read_user() -> WeatherResponse:
    return await weather_service.get_weather_data()
