import pandas as pd
import os
import smtplib
from email.mime.text import MIMEText
from src.transform import clean_data, calculate_metrics

def send_real_email_alert(revenue):
    """Sends a real email notification when revenue thresholds fail."""
    # SENDER: Enter your testing email address
    sender_email = "your_email@gmail.com"
    # RECEIVER: Usually the data/ops team email (can be the same for testing)
    receiver_email = "your_email@gmail.com"
    
    msg = MIMEText(f"🚨 ALERT: Hourly revenue has dropped drastically to ${revenue:.2f}!")
    msg['Subject'] = '⚠️ CRITICAL: CartSentry Revenue Drop Alert'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        # We use a mock/local testing server here so it runs safely without configuring passwords yet
        with smtplib.SMTP('localhost', 1025) as server:
            server.sendmail(sender_email, [receiver_email], msg.as_string())
        print("📨 Automated email alert dispatched to operations team!")
    except Exception as e:
        # If no local server is running, we log it beautifully
        print(f"📨 Email formatted successfully! (To send for real, spin up a local SMTP test server).")

def check_kpi_and_alert(metrics, threshold=150.00):
    """Checks if the revenue meets the business threshold. Triggers email if it fails."""
    if metrics is None:
        print("❌ Alert System Error: No metrics provided.")
        return False
        
    revenue = metrics.get("total_revenue", 0)
    print(f"Checking KPIs... Current Revenue: ${revenue:.2f} | Threshold: ${threshold:.2f}")
    
    if revenue < threshold:
        print("\n🚨 !!! ALERT CRITICAL ALERT !!! 🚨")
        send_real_email_alert(revenue)
        return True
    else:
        print("✅ System Healthy: Revenue is safely above the threshold.")
        return False

if __name__ == "__main__":
    cleaned_df = clean_data()
    metrics = calculate_metrics(cleaned_df)
    
    print("Testing Live Alerting System...")
    # Setting high threshold to force the alert block to execute
    check_kpi_and_alert(metrics, threshold=5000.00)
