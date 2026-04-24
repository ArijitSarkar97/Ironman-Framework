import pytest
from utils.db_util import DBUtil
from config.environment import Environment
import logging
from unittest.mock import MagicMock, patch

logger = logging.getLogger(__name__)

@pytest.fixture(scope="module")
def db_util():
    env = Environment()
    db_config = env.get_db_config()
    if not db_config:
        pytest.skip("Database configuration not found for the current environment")
    
    util = DBUtil(**db_config)
    yield util
    util.disconnect()

class TestDatabase:
    """
    Test cases for MySQL database operations.
    Note: These tests use mocking to demonstrate behavior without a live DB.
    To run against a real DB, remove the @patch decorators.
    """

    @patch('mysql.connector.connect')
    def test_db_connection(self, mock_connect, db_util):
        """Test database connection establishment."""
        db_util.connection = None  # Ensure fresh connection for test
        mock_connect.return_value.is_connected.return_value = True
        
        connection = db_util.connect()
        assert connection is not None
        assert connection.is_connected()
        logger.info("Database connection test passed")

    @patch('mysql.connector.connect')
    def test_fetch_data(self, mock_connect, db_util):
        """Test fetching data from a table."""
        db_util.connection = None  # Ensure fresh connection for test
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchall.return_value = [
            {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
            {'id': 2, 'name': 'Jane Doe', 'email': 'jane@example.com'}
        ]
        
        query = "SELECT * FROM users LIMIT 2"
        results = db_util.fetch_all(query)
        
        assert len(results) == 2
        assert results[0]['name'] == 'John Doe'
        assert results[1]['email'] == 'jane@example.com'
        logger.info("Fetch data test passed")

    @patch('mysql.connector.connect')
    def test_insert_data(self, mock_connect, db_util):
        """Test inserting data into a table."""
        db_util.connection = None  # Ensure fresh connection for test
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.rowcount = 1
        
        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        params = ('Alice', 'alice@example.com')
        affected_rows = db_util.execute_query(query, params)
        
        assert affected_rows == 1
        mock_connect.return_value.commit.assert_called_once()
        logger.info("Insert data test passed")

    @patch('mysql.connector.connect')
    def test_update_data(self, mock_connect, db_util):
        """Test updating data in a table."""
        db_util.connection = None  # Ensure fresh connection for test
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.rowcount = 1
        
        query = "UPDATE users SET email = %s WHERE name = %s"
        params = ('new_bob@example.com', 'Bob')
        affected_rows = db_util.execute_query(query, params)
        
        assert affected_rows == 1
        mock_connect.return_value.commit.assert_called_once()
        logger.info("Update data test passed")

    @patch('mysql.connector.connect')
    def test_delete_data(self, mock_connect, db_util):
        """Test deleting data from a table."""
        db_util.connection = None  # Ensure fresh connection for test
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.rowcount = 1
        
        query = "DELETE FROM users WHERE id = %s"
        params = (1,)
        affected_rows = db_util.execute_query(query, params)
        
        assert affected_rows == 1
        mock_connect.return_value.commit.assert_called_once()
        logger.info("Delete data test passed")

