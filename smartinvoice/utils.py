from decimal import Decimal, ROUND_HALF_UP, localcontext, InvalidOperation
from datetime import datetime
import requests
from requests.exceptions import RequestException


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



def safe_decimal_(value, default='0'):
    """Convert value to Decimal safely."""
    try:
        return Decimal(str(value))
    except (InvalidOperation, ValueError):
        return Decimal(default)

def calculate_unit_price_inclusive(total_inclusive_amount, rate_percent, quantity, dic_rate=0, decimal_places=2):
    """
    Safe and large-number friendly tax-exclusive price calculator.
    """
    # Early quantity validation
    if quantity in [0, '0', None]:
        raise ValueError("Quantity must be greater than zero.")

    try:
        total_inclusive = safe_decimal(total_inclusive_amount)
        rate = safe_decimal(rate_percent)
        quantity = safe_decimal(quantity)

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        with localcontext() as ctx:
            ctx.prec = 30  # High precision for large numbers
            ctx.rounding = ROUND_HALF_UP

            divisor = Decimal('1') + (rate / Decimal('100'))

            total_exclusive = (total_inclusive / divisor)
            tax_amount = total_inclusive - total_exclusive
            unit_price_exclusive = total_exclusive / quantity

            # Safe quantization using exponential format to avoid InvalidOperation
            quant = Decimal('1e-{0}'.format(decimal_places))

            total_exclusive = total_exclusive.quantize(quant)
            tax_amount = tax_amount.quantize(quant)
            unit_price_exclusive = unit_price_exclusive.quantize(quant)

        return {
            'unit_price_exclusive': unit_price_exclusive,
            'total_exclusive_amount': total_exclusive,
            'total_tax_amount': tax_amount
        }

    except (InvalidOperation, ZeroDivisionError) as e:
        raise ValueError(f"Calculation failed: {e}")

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