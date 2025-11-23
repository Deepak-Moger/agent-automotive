import unittest
import asyncio
from src.agents.diagnosis_agent import DiagnosisAgent
from src.agents.scheduling_agent import SchedulingAgent
from src.agents.manufacturing_agent import ManufacturingAgent

class TestAgents(unittest.TestCase):
    def setUp(self):
        self.diagnosis_agent = DiagnosisAgent()
        self.scheduling_agent = SchedulingAgent()
        self.manufacturing_agent = ManufacturingAgent()

    def test_diagnosis_critical(self):
        data = {"engine_temp": 120, "oil_pressure": 40}
        async def run():
            return await self.diagnosis_agent.process(data)
        result = asyncio.run(run())
        self.assertEqual(result["status"], "CRITICAL")
        self.assertIn("Engine Overheating", result["issues"])

    def test_diagnosis_healthy(self):
        data = {"engine_temp": 90, "oil_pressure": 40}
        async def run():
            return await self.diagnosis_agent.process(data)
        result = asyncio.run(run())
        self.assertEqual(result["status"], "HEALTHY")

    def test_scheduling(self):
        async def run():
            return await self.scheduling_agent.process("VIN-TEST")
        result = asyncio.run(run())
        self.assertEqual(result["status"], "CONFIRMED")
        self.assertIn("appointment_time", result)

    def test_manufacturing_feedback(self):
        diagnosis = {"issues": ["Engine Overheating"]}
        async def run():
            return await self.manufacturing_agent.process(diagnosis)
        result = asyncio.run(run())
        self.assertEqual(result["new_defects_logged"], 1)
        self.assertIn("Review cooling system", result["recommendations"][0])

if __name__ == '__main__':
    unittest.main()
