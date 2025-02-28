from fastapi import APIRouter, Request, Response, status
from pydantic import BaseModel
from typing import Dict, Optional


class Item(BaseModel):
    name: str
    description: Optional[str] = None


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class TemplateRouter:
    """
    A 'template' namespace that demonstrates the full range of HTTP methods:
    GET, POST, PUT, DELETE, PATCH, HEAD, and OPTIONS.
    Routes are under /template, with various subpaths.
    """
    def __init__(self) -> None:
        self.router = APIRouter(prefix="/template", tags=["template"])
        self.items_db: Dict[int, Item] = {}
        self.id_counter: int = 0

        self.router.add_api_route(
            "/items",
            self.list_items,
            methods=["GET"],
            summary="List all items",
            description="Retrieve a list of all items in the in-memory database."
        )
        self.router.add_api_route(
            "/items/{item_id}",
            self.get_item,
            methods=["GET"],
            summary="Get a specific item",
            description="Retrieve a single item by its ID. Returns 404 if not found."
        )
        self.router.add_api_route(
            "/items",
            self.create_item,
            methods=["POST"],
            status_code=status.HTTP_201_CREATED,
            summary="Create a new item",
            description="Create a new item with name and optional description."
        )
        self.router.add_api_route(
            "/items/{item_id}",
            self.update_item,
            methods=["PUT"],
            summary="Update an existing item",
            description="Replace the entire resource with the new data."
        )
        self.router.add_api_route(
            "/items/{item_id}",
            self.patch_item,
            methods=["PATCH"],
            summary="Partially update an existing item",
            description="Only update the specified fields of the resource."
        )
        self.router.add_api_route(
            "/items/{item_id}",
            self.delete_item,
            methods=["DELETE"],
            summary="Delete an item",
            description="Delete the specified item from the in-memory database."
        )
        self.router.add_api_route(
            "/items",
            self.head_items,
            methods=["HEAD"],
            summary="HEAD on items",
            description="Check if items endpoint is available without a body."
        )
        self.router.add_api_route(
            "/items",
            self.options_items,
            methods=["OPTIONS"],
            summary="OPTIONS on items",
            description="Return allowed methods for the /template/items endpoint."
        )

    async def list_items(self) -> Dict[str, Dict[int, Item]]:
        """Returns all items in the in-memory DB."""
        return {"items": self.items_db}

    async def get_item(self, item_id: int) -> Item:
        """Retrieve a single item by ID. Raises 404 if not found."""
        if item_id not in self.items_db:
            from fastapi import HTTPException
            raise HTTPException(status_code=404, detail="Item not found")
        return self.items_db[item_id]

    async def create_item(self, item: Item) -> Dict[str, int]:
        """
        Create a new item and store it in the in-memory DB.
        Returns the new item ID.
        """
        self.id_counter += 1
        self.items_db[self.id_counter] = item
        return {"created_id": self.id_counter}

    async def update_item(self, item_id: int, item: Item) -> Item:
        """
        Completely overwrite an existing item with the new data.
        Raises 404 if not found.
        """
        if item_id not in self.items_db:
            from fastapi import HTTPException
            raise HTTPException(status_code=404, detail="Item not found")
        self.items_db[item_id] = item
        return item

    async def patch_item(self, item_id: int, partial_item: ItemUpdate) -> Item:
        """
        Partially update an existing item. Only fields provided will be updated.
        Raises 404 if not found.
        """
        if item_id not in self.items_db:
            from fastapi import HTTPException
            raise HTTPException(status_code=404, detail="Item not found")
        stored_item = self.items_db[item_id]
        update_data = partial_item.dict(exclude_unset=True)
        updated_item = stored_item.copy(update=update_data)
        self.items_db[item_id] = updated_item
        return updated_item

    async def delete_item(self, item_id: int) -> Dict[str, str]:
        """
        Delete an item by ID. Raises 404 if not found.
        """
        if item_id not in self.items_db:
            from fastapi import HTTPException
            raise HTTPException(status_code=404, detail="Item not found")
        del self.items_db[item_id]
        return {"status": "deleted"}

    async def head_items(self, response: Response) -> None:
        """
        HEAD method to check the existence of the /items endpoint.
        Returns no body, but can set headers if needed.
        """
        response.headers["X-Items-Count"] = str(len(self.items_db))

    async def options_items(self, request: Request) -> Dict[str, list]:
        """
        OPTIONS method to return allowed HTTP methods for /items.
        """
        allowed_methods = ["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"]
        return {"allowed_methods": allowed_methods}
