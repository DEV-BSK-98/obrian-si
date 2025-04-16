import requests
from requests.exceptions import RequestException
from decimal import Decimal, getcontext, ROUND_HALF_UP

def send_api_request(method, url, headers=None, data=None, json=None, params=None, timeout=10):
    """
    Sends an HTTP request to an external API.

    :param method: HTTP method (e.g., 'GET', 'POST', 'PUT', 'DELETE')
    :param url: API endpoint
    :param headers: Dictionary of headers
    :param data: Form data (for POST, PUT, etc.)
    :param json: JSON body (for POST, PUT, etc.)
    :param params: URL query parameters
    :param timeout: Timeout in seconds
    :return: Response object or None on failure
    """
    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            data=data,
            json=json,
            params=params,
            timeout=timeout
        )
        response.raise_for_status()
        return response
    except RequestException as e:
        print(f"API request failed: {e}")
        return None

def calculate_unit_price_inclusive(total_amount, rate_percent, quantity, decimal_places=2):
    """
    Calculates the exclusive unit price from an inclusive total amount.
    Args:
        total_amount (float or str): The total amount including the percentage rate.
        rate_percent (float or str): The percentage rate (e.g. 16 for 16%).
        quantity (int): Number of units/items.
        decimal_places (int): How many decimal places to round to.
    Returns:
        Decimal: Unit price exclusive of the rate.
    """
    getcontext().prec = decimal_places + 5
    getcontext().rounding = ROUND_HALF_UP

    total_amount = Decimal(str(total_amount))
    rate_percent = Decimal(str(rate_percent))
    quantity = Decimal(str(quantity))

    if quantity == 0:
        raise ValueError("Quantity cannot be zero.")

    divisor = Decimal('1') + (rate_percent / Decimal('100'))
    exclusive_total = total_amount / divisor
    unit_price = exclusive_total / quantity

    return unit_price.quantize(Decimal('1.' + '0' * decimal_places))
