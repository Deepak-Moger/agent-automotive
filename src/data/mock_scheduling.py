import datetime
from typing import List, Dict, Any

class MockSchedulingSystem:
    def __init__(self):
        self.service_centers = ["Downtown Hub", "Westside Auto", "North Service Center"]

    def find_next_slot(self, urgency: str) -> Dict[str, Any]:
        # Simulate urgency-based scheduling
        delay_days = 1 if urgency == "CRITICAL" else 7
        next_slot = datetime.datetime.now() + datetime.timedelta(days=delay_days)
        
        # Round to nearest hour
        next_slot = next_slot.replace(minute=0, second=0, microsecond=0)
        
        return {
            "time": next_slot.isoformat(),
            "center": self.service_centers[0], # Simplification
            "duration_minutes": 60
        }
