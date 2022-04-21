from datetime import time

from fee_calculator_api.money import euro_to_cents

NO_FEE = 0

FEE_UPPER_LIMIT = euro_to_cents(15)
NO_FEE_LIMIT = euro_to_cents(100)
LOWER_CART_LIMIT = euro_to_cents(10)
MIN_DELIVERY_FEE = euro_to_cents(2)
EXTRA_DELIVERY_FEE = euro_to_cents(1)
FEE_PER_ITEM = 50

MIN_DELIVERY_DISTACE_M = 1000
EXTRA_DELIVERY_DISTACE_M = 500

NO_FEE_ITEMS_NUMBER = 4

RUSH_TIME_START = time(15, 0)
RUSH_TIME_END = time(16, 59)
RUSH_TIME_WEEKDAY_ISO = 5
RUSH_TIME_MULT = 1.1
