# import pymysql
# import os
# from dotenv import load_dotenv

# load_dotenv()


# def test_connection():
#     try:
#         timeout = 10
#         db_name = os.getenv("DB_NAME")
#         db_host = os.getenv("DB_HOST")
#         db_password = os.getenv("DB_PASSWORD")
#         db_port = os.getenv("DB_PORT")
#         db_user = os.getenv("DB_USER")

#         if None in (db_name, db_host, db_password, db_port, db_user):
#             raise ValueError("One or more required environment variables are missing.")

#         # Ensure types are correct
#         if db_port is None:
#             raise ValueError("DB_PORT environment variable is missing or invalid.")
#         db_port_int = int(db_port)

#         connection = pymysql.connect(
#             charset="utf8mb4",
#             connect_timeout=timeout,
#             cursorclass=pymysql.cursors.DictCursor,
#             db=str(db_name),
#             host=str(db_host),
#             password=str(db_password),
#             port=db_port_int,
#             user=str(db_user),
#         )

#         print("✅ Database connection successful!")

#         # Test basic operations
#         cursor = connection.cursor()
#         cursor.execute("SHOW TABLES")
#         tables = cursor.fetchall()
#         print(f"📊 Existing tables: {len(tables)}")

#         # Check if weather_data table exists and print its content
#         # The table name in the result of "SHOW TABLES" is case-insensitive in the dictionary key.
#         if any(list(d.values())[0].lower() == "weather_data" for d in tables):
#             print("\n--- Weather Data ---")
#             cursor.execute("SELECT * FROM weather_data")
#             weather_records = cursor.fetchall()
#             if weather_records:
#                 for record in weather_records:
#                     print(record)
#             else:
#                 print("No records found in weather_data table.")
#             print("--------------------")

#         connection.close()
#         return True

#     except Exception as e:
#         print(f"❌ Connection failed: {e}")
#         return False


# if __name__ == "__main__":
#     test_connection()
