from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL
db_url = "mysql+pymysql://myuser:mypassword@db:3306/user_management"

# Create the engine
engine = create_engine(db_url)

# Base for declarative models
Base = declarative_base()

# Session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
