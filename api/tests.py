"""Tests for the items app."""

from unittest import mock

from app import Item, app, items, update_items
from fastapi.testclient import TestClient

client = TestClient(app)


# ───── 1. Test pure logic ─────
def test_update_items_calculates_price_with_tax():
    """update_items adds price_with_tax when tax is provided."""
    item = Item(name="candy", description="nice chocolates", price=5, tax=1)
    result = update_items(item)
    assert result["price_with_tax"] == 6


# ───── 2. Test the real endpoint ─────
def test_get_item_endpoint():
    """GET /item/{name} returns the stored item."""
    items["foo"] = {"my": "fake item"}  # seed the in-memory store
    res = client.get("/item/foo")
    assert res.status_code == 200
    assert res.json() == {"my": "fake item"}


# ───── 3. Test with a mocked logic function ─────
def test_get_item_mocked():
    """Endpoint calls get_item — we mock it to test in isolation."""
    with mock.patch("app.get_item", return_value={"my": "faked fake item"}):
        res = client.get("/item/foo")
        assert res.status_code == 200
        assert res.json() == {"my": "faked fake item"}


# uv run pytest tests.py -v


def test_create_item_endpoint():
    """POST /items/ creates an item with tax calculation."""
    res = client.post("/items/", json={"name": "shoes", "price": 100, "tax": 20})
    assert res.status_code == 200
    assert res.json()["price_with_tax"] == 120


def test_update_items_no_tax():
    """update_items doesn't add price_with_tax when tax is None."""
    item = Item(name="free", price=10)
    result = update_items(item)
    assert "price_with_tax" not in result


def test_get_item_not_found():
    """GET /item/{name} returns 404 for unknown items."""
    res = client.get("/item/nonexistent")
    assert res.status_code == 404
