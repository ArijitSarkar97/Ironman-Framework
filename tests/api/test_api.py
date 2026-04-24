import pytest
from api_clients.user_client import UserClient

@pytest.mark.api
class TestUserAPI:
    """
    Refactored Test cases for User API using the UserClient abstraction.
    """

    @pytest.fixture(autouse=True)
    def setup(self, request):
        env_name = request.config.getoption("--env")
        self.user_client = UserClient(env_name=env_name)

    def test_get_users(self):
        """Test GET request to fetch users."""
        response = self.user_client.get_all_users()
        assert response.status_code == 200
        assert len(response.json()) > 0

    def test_get_single_user(self):
        """Test GET request to fetch a specific user."""
        user_id = 1
        response = self.user_client.get_user_by_id(user_id)
        assert response.status_code == 200
        assert response.json()['id'] == user_id

    def test_create_user(self):
        """Test POST request to create a new user."""
        user_data = {
            "name": "Antigravity",
            "username": "antigravity_ai",
            "email": "antigravity@google.com"
        }
        response = self.user_client.create_user(user_data)
        assert response.status_code in [201, 200]
        assert response.json()['name'] == user_data['name']

    def test_update_user(self):
        """Test PUT request to update an existing user."""
        user_id = 1
        updated_data = {
            "name": "Antigravity Updated",
            "email": "updated@google.com"
        }
        response = self.user_client.update_user(user_id, updated_data)
        assert response.status_code == 200
        assert response.json()['name'] == updated_data['name']

    def test_delete_user(self):
        """Test DELETE request to remove a user."""
        user_id = 1
        response = self.user_client.delete_user(user_id)
        assert response.status_code in [200, 204]
