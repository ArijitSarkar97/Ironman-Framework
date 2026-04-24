from api_clients.base_client import BaseClient

class ProductClient(BaseClient):
    """
    Client for Product related API calls.
    """
    def get_all_products(self):
        return self.util.get("/products")

    def get_product_by_id(self, product_id):
        return self.util.get(f"/products/{product_id}")
