from typing import Optional
from pydantic import BaseModel


class WeatherResponse(BaseModel):
    lon: float
    lat: float
    weather: str
    weather_description: str
    temperature: float
    perceived_temperature: float
    max_temperature: float
    min_temperature: float
    humidity: int
    visibility: int
    wind_speed: float
    wind_deg: float
    time: int

    cloudiness: Optional[str] = None
    rain_1h: Optional[str] = None
    rain_3h: Optional[str] = None
    snow_1h: Optional[str] = None
    snow_3h: Optional[str] = None
