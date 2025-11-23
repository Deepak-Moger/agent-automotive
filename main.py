import asyncio
from src.agents.master_agent import MasterAgent

async def main():
    print("Initializing Autonomous AI Agents System...")
    orchestrator = MasterAgent()
    
    # Simulate a vehicle event
    vehicle_id = "VIN-123456789"
    print(f"\n--- Processing Vehicle {vehicle_id} ---")
    result = await orchestrator.process(vehicle_id)
    
    print("\n--- Workflow Complete ---")
    print("Final Result:", result)

if __name__ == "__main__":
    asyncio.run(main())
