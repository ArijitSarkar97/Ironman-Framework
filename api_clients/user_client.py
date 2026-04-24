from api_clients.base_client import BaseClient

class UserClient(BaseClient):
    """
    Client for User related API calls.
    """
    def get_all_users(self):
        return self.util.get("/users")

    def get_user_by_id(self, user_id):
        return self.util.get(f"/users/{user_id}")

    def create_user(self, user_data):
        return self.util.post("/users", json_data=user_data)

    def update_user(self, user_id, user_data):
        return self.util.put(f"/users/{user_id}", json_data=user_data)

    def delete_user(self, user_id):
        return self.util.delete(f"/users/{user_id}")
