def calculate_congestion_level(total_containers, terminal_capacity=5000):
    """
    Returns a 'Risk Score' (0-100) based on terminal capacity.
    """
    load_percentage = (total_containers / terminal_capacity) * 100
    
    if load_percentage > 85:
        return "CRITICAL", "red"
    elif load_percentage > 60:
        return "WARNING", "orange"
    else:
        return "NORMAL", "green"

def get_action_recommendation(status, terminal_name):
    """
    Returns a specific business action based on the AI's finding.
    """
    if status == "CRITICAL":
        return f"⛔ STOP GATE ENTRY: {terminal_name} is over capacity. Reroute to Buffer Zone B."
    elif status == "WARNING":
        return f"⚠️ SLOW DOWN: {terminal_name} is busy. Notify dispatchers."
    else:
        return "✅ OPERATIONAL: Standard gate procedures apply."