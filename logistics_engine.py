def calculate_congestion_level(total_containers, extra_simulation_containers=0, terminal_capacity=5000):
    """
    Calculates risk based on REAL traffic + SIMULATED (What-If) traffic.
    Returns 3 values: Status Text, Color, and Percentage Load.
    """
    # 1. Add the hypothetical 'Chaos' to the real numbers
    simulated_total = total_containers + extra_simulation_containers
    
    # 2. Calculate the load percentage (Cap it at 100 for the progress bar, but track real load)
    load_percentage = (simulated_total / terminal_capacity) * 100
    
    # 3. Determine the status
    if load_percentage > 90:
        return "GRIDLOCK (PORT CLOSED)", "red", load_percentage
    elif load_percentage > 75:
        return "CRITICAL CONGESTION", "orange", load_percentage
    elif load_percentage > 50:
        return "HIGH TRAFFIC", "yellow", load_percentage
    else:
        return "NORMAL FLOW", "green", load_percentage

def get_action_recommendation(status, terminal_name):
    """
    Returns a specific business action based on the AI's finding.
    """
    if "GRIDLOCK" in status:
        return f"⛔ STOP GATE ENTRY: {terminal_name} is over capacity. Reroute incoming trucks to Buffer Zone B immediately."
    elif "CRITICAL" in status:
        return f"⚠️ ACTIVATE PEAK SHAVING: {terminal_name} is nearing capacity. Delay non-urgent pickups by 4 hours."
    elif "HIGH" in status:
        return f"✋ MONITOR GATES: {terminal_name} is busy. Prepare additional crane crews."
    else:
        return "✅ OPERATIONAL: Standard gate procedures apply. No delays expected."