import random
import time
from typing import Generator, Dict, Any

class TelematicsGenerator:
    def __init__(self, vehicle_id: str):
        self.vehicle_id = vehicle_id
        self.base_temp = 90
        self.base_pressure = 40

    def generate_stream(self) -> Generator[Dict[str, Any], None, None]:
        """Yields a stream of telematics data."""
        while True:
            # Simulate gradual changes or sudden spikes
            self.base_temp += random.uniform(-2, 2)
            self.base_pressure += random.uniform(-1, 1)
            
            # Introduce anomalies
            if random.random() > 0.95:
                self.base_temp += 20  # Overheating spike
            
            yield {
                "vehicle_id": self.vehicle_id,
                "timestamp": time.time(),
                "engine_temp": round(self.base_temp, 2),
                "oil_pressure": round(self.base_pressure, 2),
                "rpm": random.randint(1000, 6000),
                "speed": random.randint(0, 120),
                "error_codes": ["P0123"] if self.base_temp > 115 else []
            }
            time.sleep(0.1) # Simulate real-time delay
