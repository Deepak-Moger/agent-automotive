from typing import Dict, Any
from .base_agent import BaseAgent

class DiagnosisAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Diagnostician", role="Predictive Diagnosis")

    async def process(self, telematics_data: Dict[str, Any]) -> Dict[str, Any]:
        self.log_activity("Analyzing telematics data for defects")
        
        # Simple rule-based logic for simulation
        status = "HEALTHY"
        issues = []

        if telematics_data.get("engine_temp", 0) > 110:
            status = "CRITICAL"
            issues.append("Engine Overheating")
        elif telematics_data.get("oil_pressure", 100) < 30:
            status = "CRITICAL"
            issues.append("Low Oil Pressure")
        elif telematics_data.get("error_codes"):
            status = "WARNING"
            issues.append(f"Error Codes: {telematics_data['error_codes']}")
        
        return {
            "status": status,
            "issues": issues,
            "confidence_score": 0.95
        }
