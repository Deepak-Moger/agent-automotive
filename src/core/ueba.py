from typing import Dict, Any
import datetime

class UEBAMonitor:
    def __init__(self):
        self.logs = []
        self.anomalies = []

    def log_event(self, agent_name: str, activity: str):
        timestamp = datetime.datetime.now().isoformat()
        event = {
            "timestamp": timestamp,
            "agent": agent_name,
            "activity": activity
        }
        self.logs.append(event)
        self.analyze_behavior(event)

    def analyze_behavior(self, event: Dict[str, Any]):
        # Simple rule-based anomaly detection
        # In a real system, this would use ML models
        if "unauthorized" in event["activity"].lower():
            self.flag_anomaly(event, "Unauthorized Access Attempt")
        
        if event["agent"] == "DataAnalyzer" and "delete" in event["activity"].lower():
             self.flag_anomaly(event, "Suspicious Data Deletion")

    def flag_anomaly(self, event: Dict[str, Any], reason: str):
        print(f"[SECURITY ALERT] Anomaly detected: {reason} by {event['agent']}")
        self.anomalies.append({
            "event": event,
            "reason": reason,
            "severity": "HIGH"
        })

    def get_security_report(self):
        return {
            "total_events": len(self.logs),
            "anomalies_detected": len(self.anomalies),
            "anomalies": self.anomalies
        }
