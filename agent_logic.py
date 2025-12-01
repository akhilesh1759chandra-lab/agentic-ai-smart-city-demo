# Dummy Agentic AI Logic for Smart City Demo
# This is a simple rule-based example for concept demonstration only.

dummy_alerts = [
    {"id": 1, "type": "camera_offline", "location": "Junction-01"},
    {"id": 2, "type": "traffic_violation", "location": "RLVD-05"},
    {"id": 3, "type": "crowd_high", "location": "Market-Area"},
]

def decide_action(alert):
    if alert["type"] == "camera_offline":
        return "Create ticket for field team and inform ICCC operator."
    elif alert["type"] == "traffic_violation":
        return "Send details to traffic enforcement system and log incident."
    elif alert["type"] == "crowd_high":
        return "Notify police control room and suggest PTZ camera focus."
    else:
        return "Log and monitor."

def run_agent():
    print("=== Agentic AI – Smart City Demo ===")
    for alert in dummy_alerts:
        action = decide_action(alert)
        print(f"Alert ID: {alert['id']}, Type: {alert['type']}, Location: {alert['location']}")
        print("Suggested Action:", action)
        print("------------------------------------")

if __name__ == "__main__":
    run_agent()
