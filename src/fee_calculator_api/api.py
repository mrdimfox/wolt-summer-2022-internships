import logging
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from fee_calculator_api.model import Purchase, DeliveryFee
from fee_calculator_api.calculator import calculate_fee

log = logging.getLogger(__name__)

api = FastAPI(
    version="1.0",
    description="API for a service fee calculation.",
)


@api.post("/delivery_fee", response_model=DeliveryFee)
async def delivery_fee(purchase: Purchase):
    fee = calculate_fee(
        cart_value=purchase.cart_value,
        delivery_distance=purchase.delivery_distance,
        number_of_items=purchase.number_of_items,
        date=purchase.time,
    )

    return DeliveryFee(delivery_fee=fee)


@api.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/docs")
