from datetime import datetime

from fee_calculator_api import calculation_params as params


def calculate_fee(
    cart_value: int,
    delivery_distance: int,
    number_of_items: int,
    date: datetime,
) -> int:
    """Calculate fee by given params."""
    if cart_value >= params.NO_FEE_LIMIT:
        return params.NO_FEE

    fee = (
        _calc_cart_value_fee(cart_value)
        + _calc_items_fee(number_of_items)
        + _calc_delivery_fee(delivery_distance)
    )

    if fee >= params.FEE_UPPER_LIMIT:
        return params.FEE_UPPER_LIMIT

    if _is_rush_time(date):
        fee = round(fee * params.RUSH_TIME_MULT)

    return fee if fee < params.FEE_UPPER_LIMIT else params.FEE_UPPER_LIMIT


def _calc_cart_value_fee(cart_value: int):
    if cart_value < params.LOWER_CART_LIMIT:
        return params.LOWER_CART_LIMIT - cart_value
    return params.NO_FEE


def _calc_items_fee(number_of_items: int):
    if number_of_items > params.NO_FEE_ITEMS_NUMBER:
        return params.FEE_PER_ITEM * (number_of_items - params.NO_FEE_ITEMS_NUMBER)
    return params.NO_FEE


def _calc_delivery_fee(delivery_distance: int):
    if delivery_distance <= params.MIN_DELIVERY_DISTACE_M:
        return params.MIN_DELIVERY_FEE

    delivery_distance -= params.MIN_DELIVERY_DISTACE_M
    delivery_mult = delivery_distance // params.EXTRA_DELIVERY_DISTACE_M

    last_distance_part = delivery_distance % params.EXTRA_DELIVERY_DISTACE_M
    last_distance_mult = 1 if last_distance_part > 0 else 0

    return (
        params.EXTRA_DELIVERY_FEE * delivery_mult
        + params.EXTRA_DELIVERY_FEE * last_distance_mult
        + params.MIN_DELIVERY_FEE
    )


def _is_rush_time(date: datetime):
    return (
        date.isoweekday() == params.RUSH_TIME_WEEKDAY_ISO
        and params.RUSH_TIME_START <= date.time() <= params.RUSH_TIME_END
    )
