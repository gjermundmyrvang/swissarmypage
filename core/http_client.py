import requests

DEFAULT_TIMEOUT = 10


def get_json(
    url: str, params: dict | None = None, timeout: int = DEFAULT_TIMEOUT
) -> dict:
    response = requests.get(url, params=params, timeout=timeout)
    response.raise_for_status()
    return response.json()
