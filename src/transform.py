import pandas as pd
import os

def clean_data(input_path="data/raw_transactions.csv", output_path="data/clean_transactions.csv"):
    """Reads raw data, removes duplicates, handles missing values, and saves it."""
    if not os.path.exists(input_path):
        print(f"Error: {input_path} does not exist. Run extract.py first!")
        return None

    # 1. Load the data
    df = pd.read_csv(input_path)
    print(f"⚡ Rows loaded from raw data: {len(df)}")

    # 2. Drop duplicate transaction IDs (keeping the first occurrence)
    df = df.drop_duplicates(subset=["transaction_id"], keep="first")

    # 3. Handle missing revenue: Fill missing values with 0.0
    df["revenue"] = df["revenue"].fillna(0.0)

    # Save the cleaned data
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to {output_path}. Remaining rows: {len(df)}")
    return df

def calculate_metrics(df):
    """Aggregates data into key business metrics."""
    if df is None or df.empty:
        print("No data available to calculate metrics.")
        return

    total_revenue = df["revenue"].sum()
    total_transactions = len(df)
    
    # Calculate Conversion Rate: (Purchased / Total) * 100
    purchased_count = len(df[df["status"] == "purchased"])
    conversion_rate = (purchased_count / total_transactions) * 100 if total_transactions > 0 else 0
    
    # Calculate Cart Abandonment Rate: (Abandoned / Total) * 100
    abandoned_count = len(df[df["status"] == "abandoned"])
    abandonment_rate = (abandoned_count / total_transactions) * 100 if total_transactions > 0 else 0

    print("\n--- 📈 BUSINESS METRICS SUMMARY ---")
    print(f"Hourly Revenue: ${total_revenue:,.2f}")
    print(f"Conversion Rate: {conversion_rate:.2f}%")
    print(f"Cart Abandonment Rate: {abandonment_rate:.2f}%")
    print("-----------------------------------\n")
    
    return {
        "total_revenue": total_revenue,
        "conversion_rate": conversion_rate,
        "abandonment_rate": abandonment_rate
    }

if __name__ == "__main__":
    # Run the cleaning step, then calculate metrics
    cleaned_df = clean_data()
    calculate_metrics(cleaned_df)