from datetime import datetime
import requests
from requests.exceptions import RequestException
from decimal import Decimal, getcontext, ROUND_HALF_UP,InvalidOperation

Sales_Receipt_Type = {
    "Sale": "S",
    "Credit Note": "R",
    "Debit Note": "D"
}

Payment_Method = {
    "Cash": "01",
    "Credit": "02",
    "Cash/Credit": "03",
    "Bank Check": "04",
    "Debit & Credit Card": "05",
    "Mobile Money": "06",
    "Bank Transfer": "08",
    "Other": "07",
}

Transaction_Progress = {
    "Approved": "02",
    "Refunded": "05",
    "Transferred": "06",
    "Rejected": "04",
}

Purchase_Receipt_Type = {
    "Purchase": "P",
    "Refund after Purchase": "R",
}

Transaction_Type = {
    "Copy": "C",
    "Normal": "N",
}

Registration_Type = {
    "Automatic": "A",
    "Manual": "M",
}

Stock_In_Out = {
    "Incoming-Import": "01",
    "Incoming- Purchase": "02",
    "Incoming- Return": "03",
    "Incoming- Stock Movement": "04",
    "Incoming- Processing": "05",
    "Incoming- Adjustment": "06",
    "Outgoing- Sale": "11",
    "Outgoing- Return": "12",
    "Outgoing- Stock Movement": "13",
    "Outgoing- Processing": "14",
    "Outgoing- Discarding": "15",
    "Outgoing- Adjustment": "16"
}

Credit_Note_Reason_Code = {
    "Wrong product(s)": "01",
    "Wrong price": "02",
    "Damaged Goods": "03",
    "Wrong Customer Invoiced": "04",
    "Duplicated invoice": "05",
    "Excess supplies": "06",
    "Other (Provide other reason in brief)": "07",
}

Debit_Note_Reason = {
    "Wrong quantity invoiced": "01",
    "Wrong invoice amount": "02",
    "Omitted item": "03",
    "Other": "04",
}

Import_Item_Status = {
    "Approved": "3",
    "Rejected": "4",
}

def todaySi ():
    now = datetime.now()
    return now.strftime("%Y%m%d%H%M%S")


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

# def calculate_unit_price_inclusive(total_amount, rate_percent, quantity, decimal_places=2):
#     """
#     Calculates the exclusive unit price from an inclusive total amount.
#     Args:
#         total_amount (float or str): The total amount including the percentage rate.
#         rate_percent (float or str): The percentage rate (e.g. 16 for 16%).
#         quantity (int): Number of units/items.
#         decimal_places (int): How many decimal places to round to.
#     Returns:
#         Decimal: Unit price exclusive of the rate.
#     """
#     getcontext().prec = decimal_places + 5
#     getcontext().rounding = ROUND_HALF_UP

#     total_amount = Decimal(str(total_amount))
#     rate_percent = Decimal(str(rate_percent))
#     quantity = Decimal(str(quantity))

#     if quantity == 0:
#         raise ValueError("Quantity cannot be zero.")

#     divisor = Decimal('1') + (rate_percent / Decimal('100'))
#     exclusive_total = total_amount / divisor
#     unit_price = exclusive_total / quantity

#     return unit_price.quantize(Decimal('1.' + '0' * decimal_places))


from decimal import Decimal, getcontext, ROUND_HALF_UP

def calculate_unit_price_inclusive(total_inclusive_amount, rate_percent, quantity, dic_rate=0, decimal_places=2):
    """
    Calculates:
      1. Unit price exclusive of the tax rate
      2. Total exclusive amount (excluding tax)
      3. Tax amount

    Args:
        total_inclusive_amount (float or str): Total amount including the tax.
        rate_percent (float or str): Tax rate percentage (e.g. 16 for 16%).
        quantity (int): Number of units/items.
        decimal_places (int): Decimal places for rounding (default 2).

    Returns:
        dict: {
            'unit_price_exclusive': Decimal,
            'total_exclusive_amount': Decimal,
            'total_tax_amount': Decimal
        }
    """
    getcontext().prec = decimal_places + 5
    getcontext().rounding = ROUND_HALF_UP

    total_inclusive = Decimal(str(total_inclusive_amount))
    rate = Decimal(str(rate_percent))
    quantity = Decimal(str(quantity))

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    divisor = Decimal('1') + (rate / Decimal('100'))
    total_exclusive = (total_inclusive / divisor).quantize(Decimal('1.' + '0' * decimal_places))
    tax_amount = (total_inclusive - total_exclusive).quantize(Decimal('1.' + '0' * decimal_places))
    unit_price_exclusive = (total_exclusive / quantity).quantize(Decimal('1.' + '0' * decimal_places))

    return {
        'unit_price_exclusive': unit_price_exclusive,
        'total_exclusive_amount': total_exclusive,
        'total_tax_amount': tax_amount
    }


def safe_decimal(value, default='0.00', decimal_places=2):
    try:
        cleaned = str(value).replace(',', '').strip()
        return Decimal(cleaned).quantize(Decimal('1.' + '0' * decimal_places), rounding=ROUND_HALF_UP)
    except (InvalidOperation, ValueError, TypeError):
        return Decimal(default).quantize(Decimal('1.' + '0' * decimal_places), rounding=ROUND_HALF_UP)

def safe_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0