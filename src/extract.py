import os
import pandas as pd
from datetime import datetime, timedelta
import random

def generate_mock_data(output_path="data/raw_transactions.csv"):
    """Generates messy mock e-commerce data for pipeline testing."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    start_time = datetime.now() - timedelta(hours=6)
    data = []
    tx_ids = [f"TX{1000 + i}" for i in range(50)]
    
    for i in range(60):  
        tx_id = random.choice(tx_ids)
        timestamp = start_time + timedelta(minutes=i*6)
        
        revenue = random.choice([round(random.uniform(10.0, 150.0), 2), None]) 
        cart_status = random.choice(["purchased", "abandoned", "purchased"])
        
        if cart_status == "abandoned":
            revenue = 0.0 if random.random() > 0.5 else None
            
        data.append({
            "transaction_id": tx_id,
            "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "revenue": revenue,
            "status": cart_status
        })
        
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    print(f"Successfully extracted and saved raw data to {output_path}")
    return output_path

if __name__ == "__main__":
    generate_mock_data()