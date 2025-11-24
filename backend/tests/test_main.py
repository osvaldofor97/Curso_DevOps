import os, sys
import pytest
from httpx import AsyncClient, ASGITransport

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import app


@pytest.mark.asyncio
async def test_read_root():
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/")

    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


if __name__ == "__main":
    pytest.main()
