from api_clients.base_client import BaseClient

class AuthClient(BaseClient):
    """
    Client for Authentication related API calls.
    """
    def login(self, username, password):
        """
        Sends a login request and returns the response.
        """
        payload = {
            "username": username,
            "password": password
        }
        # Assuming the endpoint is /login based on our mock server
        return self.util.post("/login", json_data=payload)

    def get_token(self, username, password):
        """
        Helper method to directly get the auth token.
        """
        response = self.login(username, password)
        if response.status_code == 200:
            return response.json().get("token")
        return None
