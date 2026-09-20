import requests
from core.errors import ToolAPIError
from core.http_client import get_json
from .models import ConversionResult

BASE_URL = "https://api.frankfurter.dev"
COMMON_CURRENCIES = ["USD", "EUR", "GBP", "JPY", "NOK", "SEK", "CHF", "CAD", "AUD"]


def convert(amount: float, from_currency: str, to_currency: str) -> ConversionResult:
    if from_currency == to_currency:
        return ConversionResult(amount, from_currency, to_currency, 1.0, amount, "—")

    try:
        data = get_json(
            f"{BASE_URL}/v2/rate/{from_currency}/{to_currency}",
        )
    except requests.RequestException as e:
        raise ToolAPIError(f"Conversion request failed: {e}") from e

    try:
        rate = data["rate"]
        converted_amount = round(amount * rate, 2)
        return ConversionResult(
            amount=amount,
            from_currency=data["base"],
            to_currency=to_currency,
            rate=rate,
            converted_amount=converted_amount,
            date=data["date"],
        )
    except KeyError as e:
        raise ToolAPIError(f"Unexpected response shape: {e}") from e


def get_currencies():
    try:
        data = get_json(f"{BASE_URL}/v2/currencies")
        currencies = [c["iso_code"] for c in data]
        sorted_by_common = list(dict.fromkeys(COMMON_CURRENCIES + currencies))
        return sorted_by_common

    except requests.RequestException as e:
        raise ToolAPIError(f"Request for currencies failed: {e}") from e
