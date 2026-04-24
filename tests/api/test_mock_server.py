import pytest
from utils.api_util import APIUtil
from config.environment import Environment

@pytest.fixture(scope="module")
def api_util(request):
    env_name = request.config.getoption("--env")
    env = Environment(env_name=env_name)
    api_config = env.get_api_config()
    return APIUtil(base_url=api_config['base_url'])

class TestMockServer:
    """
    Test cases to verify the standalone Mock API Server.
    Run these tests with: pytest tests/test_mock_server.py --env=mock
    """

    def test_mock_health(self, api_util):
        """Verify the mock server is healthy."""
        response = api_util.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}

    def test_get_mock_products(self, api_util):
        """Verify fetching products from the mock server."""
        response = api_util.get("/products")
        assert response.status_code == 200
        assert len(response.json()) > 0
        assert response.json()[0]["name"] == "OrangePet Premium Dog Food"

    def test_mock_login_success(self, api_util):
        """Verify successful login on the mock server."""
        login_data = {"username": "admin", "password": "password"}
        response = api_util.post("/login", json_data=login_data)
        assert response.status_code == 200
        assert "token" in response.json()

    def test_mock_login_failure(self, api_util):
        """Verify failed login on the mock server."""
        login_data = {"username": "wrong", "password": "wrong"}
        response = api_util.post("/login", json_data=login_data)
        assert response.status_code == 401
