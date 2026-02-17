import pandas as pd
import numpy as np

def fetch_port_data():
    """
    Simulates fetching live data from the Port of Antwerp API.
    """
    np.random.seed(42) # Keeps data consistent for demo
    
    data = {
        'vessel_id': [f"VSL-{i}" for i in range(1000, 1100)],
        'terminal': np.random.choice(['Deurganckdok', 'MPET', 'Kallo Lock', 'Noordzee'], 100),
        'status': np.random.choice(['On Time', 'Delayed', 'Cancelled'], 100, p=[0.7, 0.2, 0.1]),
        'containers': np.random.randint(50, 1500, 100), # Random cargo size
        'eta_offset': np.random.randint(-2, 10, 100) # Hours from now
    }
    
    return pd.DataFrame(data)

def clean_data(df):
    """
    Removes cancelled ships and prepares the data.
    """
    # remove cancelled ships (they don't cause congestion)
    df = df[df['status'] != 'Cancelled']
    return df