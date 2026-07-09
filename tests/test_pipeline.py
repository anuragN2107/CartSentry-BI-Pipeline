import pytest
import pandas as pd
from src.transform import clean_data
from src.alert import check_kpi_and_alert

def test_duplicate_transactions_are_dropped(tmp_path):
    """Test that our transformation logic successfully drops duplicate transaction IDs."""
    # Create a small sample of fake messy data with a duplicate ID (TX100)
    fake_data = pd.DataFrame({
        "transaction_id": ["TX100", "TX100", "TX101"],
        "timestamp": ["2026-01-01 10:00:00", "2026-01-01 10:05:00", "2026-01-01 10:10:00"],
        "revenue": [50.0, 50.0, 30.0],
        "status": ["purchased", "purchased", "purchased"]
    })
    
    # Save it to a temporary test folder provided by pytest
    raw_path = tmp_path / "test_raw.csv"
    clean_path = tmp_path / "test_clean.csv"
    fake_data.to_csv(raw_path, index=False)
    
    # Run our cleaning function on it
    cleaned_df = clean_data(input_path=str(raw_path), output_path=str(clean_path))
    
    # Assert (Check): The rows should go from 3 rows down to 2 rows because TX100 was duplicated!
    assert len(cleaned_df) == 2
    print("✅ Test Passed: Duplicates were successfully dropped!")

def test_alert_triggers_when_revenue_is_zero():
    """Test that our alerting logic triggers correctly if revenue drops below threshold."""
    # Set up mock metrics where revenue is exactly $0.00
    broken_site_metrics = {
        "total_revenue": 0.0,
        "conversion_rate": 0.0,
        "abandonment_rate": 100.0
    }
    
    # Check if an alert triggers given a threshold of $150.00
    alert_triggered = check_kpi_and_alert(broken_site_metrics, threshold=150.00)
    
    # Assert (Check): alert_triggered must equal True
    assert alert_triggered is True
    print("✅ Test Passed: Alert correctly triggered for zero revenue!")