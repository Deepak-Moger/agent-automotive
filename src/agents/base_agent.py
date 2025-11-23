from abc import ABC, abstractmethod
from typing import Any, Dict, List

class BaseAgent(ABC):
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.memory: List[Dict[str, Any]] = []

    @abstractmethod
    async def process(self, input_data: Any) -> Any:
        """Process the input data and return a result."""
        pass

    def log_activity(self, activity: str):
        """Log agent activity for UEBA monitoring."""
        # In a real system, this would send data to the Security Layer
        print(f"[UEBA LOG] Agent: {self.name}, Role: {self.role}, Activity: {activity}")
        self.memory.append({"activity": activity, "timestamp": "TODO: timestamp"})

    def get_state(self) -> Dict[str, Any]:
        return {"name": self.name, "memory": self.memory}
