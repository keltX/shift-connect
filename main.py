from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any
import json
from datetime import datetime
import os

app = FastAPI()

class DataModel(BaseModel):
    data: Any

@app.head("/")
async def handle_head():
    return {"message": "OK"}

@app.post("/push/")
async def receive_data(item: DataModel):
    # Generate a unique filename using the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"data_{timestamp}.json"
    
    print(json.dumps(item))
    """# Define the path to save the file
    # Use the mounted persistent disk directory
    file_path = os.path.join("/var/data", "data", filename)
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Save the data as a JSON file
    with open(file_path, "w") as f:
        json.dump(item.dict(), f, indent=4)
    
    return {"message": "Data received and saved successfully", "filename": filename}"""

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)