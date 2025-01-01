from fastapi import FastAPI
from routes.api.user import router as user_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from pathlib import Path

# Initialize the FastAPI app
app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(user_router, prefix="/api")

# Load .env file explicitly
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

print("MONGO_URI:", os.getenv("MONGO_URI"))
print("DATABASE_NAME:", os.getenv("DATABASE_NAME"))

@app.get("/")
async def root():
    return {"message": "Welcome to the Chris Iyer's first python server!"}

# MongoDB Connection Health Check
@app.get("/health")
async def health_check():
    try:
        # Check MongoDB connection
        MONGO_URI = os.getenv("MONGO_URI")
        client = AsyncIOMotorClient(MONGO_URI)
        await client.admin.command("ping")  # Ping the database
        return {"status": "Connected to MongoDB"}
    except Exception as e:
        return {"status": "Not connected", "error": str(e)}




# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
