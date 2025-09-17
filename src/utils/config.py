import os
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv
load_dotenv(override=True)


@dataclass
class Settings:
    geoapify_api_key: Optional[str] = os.getenv("GEOAPIFY_API_KEY")
    places_endpoint: str = os.getenv("PLACES_API_ENDPOINT", "https://api.geoapify.com/v2/places")
    geocode_endpoint: str = os.getenv("GEOCODE_API_ENDPOINT", "https://api.geoapify.com/v1/geocode/search")
    isoline_endpoint: str = os.getenv("ISOLINE_API_ENDPOINT", "https://api.geoapify.com/v1/isoline")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    http_timeout_seconds: int = int(os.getenv("HTTP_TIMEOUT_SECONDS", "15"))
    retry_max_attempts: int = int(os.getenv("RETRY_MAX_ATTEMPTS", "3"))


settings = Settings()


