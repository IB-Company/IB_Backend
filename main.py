from fastapi import FastAPI

from controller import exchange_rate_controller
from controller.weather.weather_controller import weather_controller
from dotenv import load_dotenv
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=env_path, verbose=True)

app = FastAPI()
app.include_router(exchange_rate_controller.router)
app.include_router(weather_controller)
