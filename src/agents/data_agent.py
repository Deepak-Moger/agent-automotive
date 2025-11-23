from typing import Dict, Any
from .base_agent import BaseAgent
from ..data.telematics_generator import TelematicsGenerator
import random

class DataAnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="DataAnalyzer", role="Data Analysis")

    async def process(self, vehicle_id: str) -> Dict[str, Any]:
        self.log_activity(f"Fetching telematics for {vehicle_id}")
        
        # Use the generator to get a single data point for simulation
        generator = TelematicsGenerator(vehicle_id)
        data_point = next(generator.generate_stream())
        
        return data_point
