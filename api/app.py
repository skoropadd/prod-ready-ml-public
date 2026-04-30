"""Item management app — combines Pydantic models, business logic, and API endpoints."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Item(BaseModel):
    """Pydantic model for an item."""

    name: str
    description: str | None = None
    price: float
    tax: float | None = None


# In-memory "database"
items: dict[str, dict] = {}


def update_items(item: Item) -> dict:
    """Add or update an item, calculating price_with_tax if applicable."""
    item_dict = item.model_dump()
    if item.tax:
        item_dict["price_with_tax"] = item.price + item.tax
    items[item.name] = item_dict
    return item_dict


def get_item(item_name: str) -> dict | None:
    """Look up an item by name."""
    return items.get(item_name)


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    """Create or update an item."""
    return update_items(item)


@app.get("/item/{item_name}")
async def serve_item(item_name: str):
    """Get an item by name."""
    item = get_item(item_name)
    if item is None:
        raise HTTPException(404, f"can't find {item_name}")
    return item
