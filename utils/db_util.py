import mysql.connector
from mysql.connector import Error
import logging

logger = logging.getLogger(__name__)

class DBUtil:
    """
    Utility class for MySQL database operations.
    """

    def __init__(self, host, user, password, database, port=3306):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': port
        }
        self.connection = None

    def connect(self):
        """Establish a database connection."""
        try:
            if self.connection is None or not self.connection.is_connected():
                self.connection = mysql.connector.connect(**self.config)
                logger.info("Successfully connected to the database")
            return self.connection
        except Error as e:
            logger.error(f"Error while connecting to MySQL: {e}")
            raise

    def disconnect(self):
        """Close the database connection."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            logger.info("MySQL connection is closed")

    def execute_query(self, query, params=None):
        """Execute a query (INSERT, UPDATE, DELETE)."""
        cursor = None
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            affected_rows = cursor.rowcount
            logger.info(f"Query executed successfully. Affected rows: {affected_rows}")
            return affected_rows
        except Error as e:
            logger.error(f"Failed to execute query: {e}")
            if self.connection:
                self.connection.rollback()
            raise
        finally:
            if cursor:
                cursor.close()

    def fetch_all(self, query, params=None):
        """Execute a SELECT query and fetch all results."""
        cursor = None
        try:
            self.connect()
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params)
            results = cursor.fetchall()
            logger.info(f"Query executed successfully. Fetched {len(results)} rows")
            return results
        except Error as e:
            logger.error(f"Failed to fetch results: {e}")
            raise
        finally:
            if cursor:
                cursor.close()

    def fetch_one(self, query, params=None):
        """Execute a SELECT query and fetch one result."""
        cursor = None
        try:
            self.connect()
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params)
            result = cursor.fetchone()
            logger.info("Query executed successfully. Fetched one row")
            return result
        except Error as e:
            logger.error(f"Failed to fetch result: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
