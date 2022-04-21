import pytest
from httpx import AsyncClient

from fee_calculator_api import api


@pytest.mark.asyncio
async def test_delivery_fee():
    async with AsyncClient(app=api, base_url="http://test") as client:
        response = await client.post(
            "/delivery_fee",
            json={
                "cart_value": 790,
                "delivery_distance": 2235,
                "number_of_items": 4,
                "time": "2021-10-12T13:00:00Z",
            },
        )

    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 710}


@pytest.mark.asyncio
async def test_delivery_fee_422():
    async with AsyncClient(app=api, base_url="http://test") as client:
        response = await client.post(
            "/delivery_fee",
            json={
                "cart_value": -1,
                "delivery_distance": -1,
                "number_of_items": -1,
                "time": "2021-10-12",
            },
        )

        fields = response.json()["detail"]

    assert response.status_code == 422
    assert len(fields) == 4, "All fields should be forbidden"
    assert all(
        ["value_error" in f["type"] for f in fields]
    ), "All fields should have value_error responce type"
