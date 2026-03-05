from sqlalchemy import create_engine, MetaData

# Database connection setup
DATABASE_URL = "sqlite:///./test.db"  # Replace with your actual database URL
e
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Connect to the database
with engine.connect() as connection:
    print("Connected to the database!")
    # Perform database operations here
