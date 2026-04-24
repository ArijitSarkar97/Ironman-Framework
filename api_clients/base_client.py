import logging
from utils.api_util import APIUtil
from config.environment import Environment

class BaseClient:
    """
    Base API Client that handles configuration and environment setup.
    All specific clients (Auth, Product, etc.) should inherit from this.
    """
    def __init__(self, env_name=None, token=None):
        self.env = Environment(env_name=env_name)
        self.api_config = self.env.get_api_config()
        self.base_url = self.api_config['base_url']
        self.util = APIUtil(base_url=self.base_url)
        self.logger = logging.getLogger(self.__class__.__name__)
        
        if token:
            self.util.set_token(token)

    def set_headers(self, headers):
        """Add or update headers."""
        self.headers.update(headers)

    def set_token(self, token, auth_type="Bearer"):
        """Convenience method to set the Authorization header."""
        self.set_headers({"Authorization": f"{auth_type} {token}"})
