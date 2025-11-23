from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from src.agents.master_agent import MasterAgent
from src.data.telematics_generator import TelematicsGenerator
import asyncio
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (Dashboard)
app.mount("/static", StaticFiles(directory="src/ui/static"), name="static")

orchestrator = MasterAgent()

@app.get("/")
async def root():
    return {"message": "Autonomous AI Agents API is running"}

@app.get("/process/{vehicle_id}")
async def process_vehicle(vehicle_id: str):
    result = await orchestrator.process(vehicle_id)
    return result

@app.websocket("/ws/telematics/{vehicle_id}")
async def websocket_endpoint(websocket: WebSocket, vehicle_id: str):
    await websocket.accept()
    generator = TelematicsGenerator(vehicle_id)
    try:
        for data in generator.generate_stream():
            await websocket.send_text(json.dumps(data))
            await asyncio.sleep(1) # Slow down for demo
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()
