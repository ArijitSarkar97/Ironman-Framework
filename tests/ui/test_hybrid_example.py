import pytest
from api_clients.product_client import ProductClient

@pytest.mark.hybrid
class TestHybridAutomation:
    """
    Demonstrates Hybrid Automation (UI + API Integration)
    """

    @pytest.fixture(autouse=True)
    def setup(self, request):
        env_name = request.config.getoption("--env")
        self.product_api = ProductClient(env_name=env_name)

    def test_ui_action_with_api_validation(self, api_authenticated_driver):
        """
        1. Login via API & Inject Token (handled by fixture)
        2. Verify UI state
        3. Validate against API data
        """
        driver = api_authenticated_driver
        
        # Scenario: We are logged in. Let's say we check a product details page.
        # For this demo, we'll just check if we can reach the home page without redirected to login.
        assert "Practice Page" in driver.title or "Automation" in driver.title
        
        # Now validate backend data using API
        response = self.product_api.get_product_by_id(1)
        assert response.status_code == 200
        api_product_name = response.json()["name"]
        
        print(f"Validated UI action against Backend API. Product Name: {api_product_name}")
        assert api_product_name == "OrangePet Premium Dog Food"
