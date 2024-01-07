from fastapi import FastAPI
from database import engine, create_database
import models  # Import models to register them

app = FastAPI()


# Create the database tables
create_database()