from typing import Dict, Any
from .base_agent import BaseAgent
from .data_agent import DataAnalysisAgent
from .diagnosis_agent import DiagnosisAgent
from .scheduling_agent import SchedulingAgent
from .customer_agent import CustomerEngagementAgent
from .manufacturing_agent import ManufacturingAgent
from ..core.ueba import UEBAMonitor

class MasterAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="MasterOrchestrator", role="Orchestrator")
        self.data_agent = DataAnalysisAgent()
        self.diagnosis_agent = DiagnosisAgent()
        self.scheduling_agent = SchedulingAgent()
        self.customer_agent = CustomerEngagementAgent()
        self.manufacturing_agent = ManufacturingAgent()
        self.ueba = UEBAMonitor()

    def log_activity(self, activity: str):
        # Override to send to UEBA
        super().log_activity(activity)
        if hasattr(self, 'ueba'):
            self.ueba.log_event(self.name, activity)

    async def process(self, vehicle_id: str) -> Dict[str, Any]:
        self.log_activity(f"Starting workflow for vehicle {vehicle_id}")
        
        # Step 1: Data Analysis
        telematics_data = await self.data_agent.process(vehicle_id)
        self.log_activity(f"Data analysis complete for {vehicle_id}")

        # Step 2: Diagnosis
        diagnosis = await self.diagnosis_agent.process(telematics_data)
        self.log_activity(f"Diagnosis complete: {diagnosis.get('status')}")

        result = {
            "vehicle_id": vehicle_id,
            "diagnosis": diagnosis,
            "actions_taken": []
        }

        # Step 3: Decision Logic
        if diagnosis.get("status") == "CRITICAL":
            # Schedule immediately
            appointment = await self.scheduling_agent.process(vehicle_id)
            result["appointment"] = appointment
            self.log_activity("Scheduled emergency appointment")
            
            # Notify Customer
            notification = await self.customer_agent.process({
                "vehicle_id": vehicle_id, 
                "message": "Critical issue detected. Appointment scheduled."
            })
            result["customer_notification"] = notification

        elif diagnosis.get("status") == "WARNING":
            # Just notify
            notification = await self.customer_agent.process({
                "vehicle_id": vehicle_id, 
                "message": "Maintenance warning. Please schedule service soon."
            })
            result["customer_notification"] = notification

        # Step 4: Manufacturing Feedback
        if diagnosis.get("issues"):
            feedback = await self.manufacturing_agent.process(diagnosis)
            result["manufacturing_feedback"] = feedback
            self.log_activity("Sent feedback to manufacturing")

        return result
