from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = "users"

client= AsyncIOMotorClient(MONGO_URL)
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]

async def create_user(user):
     user_dict = user.dict()
     result = await collection.insert_one(user_dict)
     if result.inserted_id:
          return {"id": str(result.inserted_id),"name": user.name}
     raise HTTPException(status_code=500, detail="Failed to create user")