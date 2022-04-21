from pydantic import BaseModel, validator
from pydantic.fields import ModelField
from datetime import datetime


def _positive_int(name: str, value: int):
    if value < 0:
        raise ValueError(f"{name} must be positive number")
    return value


class Purchase(BaseModel):
    """'/delivery_fee' endpoint request data scheme."""

    cart_value: int
    delivery_distance: int
    number_of_items: int
    time: datetime

    @validator("cart_value", "delivery_distance", "number_of_items")
    @classmethod
    def must_be_positive(cls, value: int, values, field: ModelField):
        return _positive_int(field.name, value)


class DeliveryFee(BaseModel):
    """'/delivery_fee' endpoint responce data scheme."""

    delivery_fee: int
