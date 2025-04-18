from decimal import Decimal, getcontext, ROUND_HALF_UP

def calculate_unit_price_inclusive(total_inclusive_amount, rate_percent, quantity, decimal_places=2):
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


print(calculate_unit_price_inclusive (116, 16, 10))