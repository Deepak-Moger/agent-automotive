from typing import Dict, Any

class MockCRM:
    def __init__(self):
        self.customers = {
            "VIN-123456789": {
                "name": "John Doe",
                "email": "john.doe@example.com",
                "phone": "+1-555-0101",
                "preferred_channel": "email"
            },
            "VIN-987654321": {
                "name": "Jane Smith",
                "email": "jane.smith@example.com",
                "phone": "+1-555-0202",
                "preferred_channel": "sms"
            }
        }

    def get_customer_profile(self, vehicle_id: str) -> Dict[str, Any]:
        return self.customers.get(vehicle_id, {
            "name": "Unknown Owner",
            "email": "unknown@example.com",
            "phone": "N/A",
            "preferred_channel": "app_notification"
        })
