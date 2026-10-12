import sys
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

password = quote_plus("Rishi@2003")

# 1. Connect to the root server first (without specifying a database)
BASE_URL = f"mysql+pymysql://root:{password}@127.0.0.1:3306/"
# 2. Target URL for later verification
DATABASE_URL = f"mysql+pymysql://root:{password}@127.0.0.1:3306/fastapi_db"

try:
    print("🔄 Connecting to MySQL server to create database...")
    base_engine = create_engine(BASE_URL)
    
    # Create the database if it doesn't exist
    with base_engine.connect() as connection:
        connection.execute(text("CREATE DATABASE IF NOT EXISTS fastapi_db;"))
        print("📁 Database 'fastapi_db' is ready!")

    print("🔄 Verifying connection to 'fastapi_db'...")
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        result = connection.execute(text("SELECT VERSION();"))
        mysql_version = result.fetchone()
        
    print("✅ Connection Successful!")
    print(f"🖥️  MySQL Version: {mysql_version}")

except Exception as e:
    print("❌ Connection Failed!")
    print(f"⚠️  Error details: {e}")
    sys.exit(1)
