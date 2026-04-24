import requests
import logging
import json

logger = logging.getLogger(__name__)

class APIUtil:
    """
    Utility class for REST API operations.
    """

    def __init__(self, base_url, timeout=30):
        self.base_url = base_url
        self.timeout = timeout
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def set_headers(self, headers):
        """Add or update headers."""
        self.headers.update(headers)

    def set_token(self, token, auth_type="Bearer"):
        """Convenience method to set the Authorization header."""
        self.set_headers({"Authorization": f"{auth_type} {token}"})

    def _log_request(self, method, url, **kwargs):
        """Log the outgoing request."""
        logger.info(f"API Request: {method} {url}")
        if 'json' in kwargs:
            logger.debug(f"Payload: {json.dumps(kwargs['json'], indent=2)}")
        elif 'data' in kwargs:
            logger.debug(f"Data: {kwargs['data']}")

    def _log_response(self, response):
        """Log the incoming response."""
        logger.info(f"API Response Status: {response.status_code}")
        try:
            logger.debug(f"Response Body: {json.dumps(response.json(), indent=2)}")
        except ValueError:
            logger.debug(f"Response Body: {response.text}")

    def get(self, endpoint, params=None, **kwargs):
        """Perform a GET request."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        self._log_request("GET", url, params=params, **kwargs)
        response = requests.get(url, params=params, headers=self.headers, timeout=self.timeout, **kwargs)
        self._log_response(response)
        return response

    def post(self, endpoint, data=None, json_data=None, **kwargs):
        """Perform a POST request."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        self._log_request("POST", url, data=data, json=json_data, **kwargs)
        response = requests.post(url, data=data, json=json_data, headers=self.headers, timeout=self.timeout, **kwargs)
        self._log_response(response)
        return response

    def put(self, endpoint, data=None, json_data=None, **kwargs):
        """Perform a PUT request."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        self._log_request("PUT", url, data=data, json=json_data, **kwargs)
        response = requests.put(url, data=data, json=json_data, headers=self.headers, timeout=self.timeout, **kwargs)
        self._log_response(response)
        return response

    def delete(self, endpoint, **kwargs):
        """Perform a DELETE request."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        self._log_request("DELETE", url, **kwargs)
        response = requests.delete(url, headers=self.headers, timeout=self.timeout, **kwargs)
        self._log_response(response)
        return response
