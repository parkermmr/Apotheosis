import pytest
from fastapi.testclient import TestClient
from app.app import App


@pytest.fixture
def client():
    """
    Creates a new TestClient instance for each test,
    ensuring a fresh in-memory database for the TemplateRouter.
    """
    app = App()
    return TestClient(app)


def test_list_items_empty(client):
    response = client.get("/template/items")
    assert response.status_code == 200
    data = response.json()
    assert data == {"items": {}}


def test_create_item(client):
    payload = {"name": "Test Item", "description": "Just a test"}
    response = client.post("/template/items", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "created_id" in data
    created_id = data["created_id"]

    get_response = client.get(f"/template/items/{created_id}")
    assert get_response.status_code == 200
    assert get_response.json() == payload


def test_get_nonexistent_item(client):
    response = client.get("/template/items/9999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Item not found"


def test_update_item(client):
    create_res = client.post("/template/items", json={"name": "Old Name"})
    created_id = create_res.json()["created_id"]

    update_payload = {"name": "New Name", "description": "Updated description"}
    update_res = client.put(f"/template/items/{created_id}", json=update_payload)
    assert update_res.status_code == 200
    updated_data = update_res.json()
    assert updated_data == update_payload

    get_res = client.get(f"/template/items/{created_id}")
    assert get_res.status_code == 200
    assert get_res.json() == update_payload


def test_update_item_404(client):
    response = client.put("/template/items/9999", json={"name": "Missing"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_patch_item(client):
    create_res = client.post("/template/items", json={"name": "Patch Me"})
    created_id = create_res.json()["created_id"]

    patch_payload = {"description": "Patched description"}
    patch_res = client.patch(f"/template/items/{created_id}", json=patch_payload)
    assert patch_res.status_code == 200
    patched_data = patch_res.json()
    assert patched_data["name"] == "Patch Me"
    assert patched_data["description"] == "Patched description"

    get_res = client.get(f"/template/items/{created_id}")
    assert get_res.status_code == 200
    assert get_res.json() == patched_data


def test_patch_item_404(client):
    response = client.patch("/template/items/9999", json={"name": "Does Not Exist"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_delete_item(client):
    create_res = client.post("/template/items", json={"name": "To Delete"})
    created_id = create_res.json()["created_id"]

    del_res = client.delete(f"/template/items/{created_id}")
    assert del_res.status_code == 200
    assert del_res.json() == {"status": "deleted"}

    get_res = client.get(f"/template/items/{created_id}")
    assert get_res.status_code == 404


def test_delete_item_404(client):
    del_res = client.delete("/template/items/9999")
    assert del_res.status_code == 404
    assert del_res.json()["detail"] == "Item not found"


def test_head_items(client):
    client.post("/template/items", json={"name": "HeadTest"})
    response = client.head("/template/items")
    assert response.status_code == 200
    assert not response.content
    assert "X-Items-Count" in response.headers
    assert response.headers["X-Items-Count"] == "1"


def test_options_items(client):
    response = client.options("/template/items")
    assert response.status_code == 200
    data = response.json()
    assert "allowed_methods" in data
    assert sorted(data["allowed_methods"]) == [
        "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"
    ]
