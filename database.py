import pymysql
import os
from dotenv import load_dotenv

load_dotenv()


class WeatherDatabase:
    def __init__(self):
        # Load environment variables
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")
        self.port = int(os.getenv("DB_PORT", "3306"))
        self.connection = None

        # Validate required environment variables
        if not all([self.host, self.user, self.password, self.database]):
            raise ValueError("Missing required database environment variables")

    def connect(self):
        """Create database connection"""
        try:
            timeout = 10
            self.connection = pymysql.connect(
                host=str(self.host),
                user=str(self.user),
                password=str(self.password),
                db=str(self.database),
                port=self.port,
                charset="utf8mb4",
                connect_timeout=timeout,
                read_timeout=timeout,
                write_timeout=timeout,
                cursorclass=pymysql.cursors.DictCursor,
            )
            print("✅ Database connection successful!")
            return True
        except pymysql.MySQLError as e:
            print(f"❌ Database connection failed: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error connecting to database: {str(e)}")
            return False

    def create_tables(self):
        """Create necessary tables"""
        if not self.connection:
            return
        try:
            cursor = self.connection.cursor()

            # Create weather_data table
            create_table_query = """
            CREATE TABLE IF NOT EXISTS weather_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                city VARCHAR(100) NOT NULL,
                state VARCHAR(50) DEFAULT 'Gujarat',
                temperature DECIMAL(5,2),
                feels_like DECIMAL(5,2),
                humidity INT,
                pressure DECIMAL(7,2),
                description VARCHAR(255),
                wind_speed DECIMAL(5,2),
                INDEX idx_city (city)
            )
            """
            cursor.execute(create_table_query)
            self.connection.commit()
            print("✅ Tables created successfully")

        except pymysql.MySQLError as e:
            print(f"❌ Error creating tables: {e}")

    def insert_weather_data(self, weather_data):
        """Insert weather data into database"""
        if not self.connection:
            return None
        try:
            cursor = self.connection.cursor()
            insert_query = """
            INSERT INTO weather_data (city, temperature, feels_like, humidity, 
                                    pressure, description, wind_speed)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, weather_data)
            self.connection.commit()
            return cursor.lastrowid
        except pymysql.MySQLError as e:
            print(f"❌ Error inserting data: {e}")
            return None

    def get_weather_history(self, city, limit=10):
        """Get weather history for a city"""
        if not self.connection:
            return []
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT city, temperature, feels_like, humidity, pressure, 
                   description, wind_speed
            FROM weather_data 
            WHERE city = %s 
            ORDER BY id DESC 
            LIMIT %s
            """
            cursor.execute(query, (city, limit))
            return cursor.fetchall()
        except pymysql.MySQLError as e:
            print(f"❌ Error fetching data: {e}")
            return []

    def get_weather_by_city(self, city):
        """Get all weather data for a specific city"""
        if not self.connection:
            return []
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM weather_data WHERE city = %s ORDER BY id DESC"
            cursor.execute(query, (city,))
            return cursor.fetchall()
        except pymysql.MySQLError as e:
            print(f"❌ Error fetching data for city {city}: {e}")
            return []

    def get_all_cities_with_data(self):
        """Get list of cities that have weather data"""
        if not self.connection:
            return []
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT DISTINCT city, COUNT(*) as record_count
            FROM weather_data 
            GROUP BY city
            ORDER BY city
            """
            cursor.execute(query)
            return cursor.fetchall()
        except pymysql.MySQLError as e:
            print(f"❌ Error fetching cities: {e}")
            return []

    def get_all_weather_data(self):
        """Get all weather data from the database"""
        if not self.connection:
            return []
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM weather_data ORDER BY id DESC"
            cursor.execute(query)
            return cursor.fetchall()
        except pymysql.MySQLError as e:
            print(f"❌ Error fetching all weather data: {e}")
            return []

    def close(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
            print("✅ MySQL connection closed")
