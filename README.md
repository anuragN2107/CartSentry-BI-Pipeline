# 🛒 CartSentry: Automated E-Commerce Metric Pipeline & KPI Alerting

A production-ready Business Intelligence engineering project that moves away from static, standalone analysis to build a fully automated data pipeline, data quality assurance test suite, automated alerting infrastructure, and dynamic visualization layer.

## 🏗️ System Architecture & Workflow

The platform handles real-world transactional complexities (missing fields, duplicate ingestion) using a modular design:

1. **Extraction (`src/extract.py`)**: Simulates streaming transactional data, introducing duplicate IDs and null financial fields to mimic messy production sources.
2. **Transformation (`src/transform.py`)**: Utilizes Pandas to perform analytical data cleaning, drop duplicate keys, impute null values, and calculate core business KPIs (Hourly Revenue, Conversion Rates, Cart Abandonment).
3. **Alerting Engine (`src/alert.py`)**: Monitors critical performance drops and automatically formats automated operational notifications if hourly sales tank.
4. **Interactive Dashboard (`src/dashboard.py`)**: Implements an interactive Streamlit user interface to render live metric trends, transactional state splits, and data health matrices.
5. **Automation Testing (`tests/`)**: Employs Pytest to implement unit tests validating data deduplication and alerting behaviors.

---

## 🛠️ Tech Stack & Tools
* **Language:** Python 3.11+
* **Data Engineering:** Pandas
* **Quality Assurance:** Pytest
* **BI Visualization:** Streamlit
* **Version Control:** Git / GitHub

---

## 🚀 Getting Started & Execution

### 1. Initialize the Environment
```powershell
# Clone or navigate to the workspace, create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install requirements
pip install pandas pytest streamlit requests
```

### 2. Run the Data Pipeline Sequence
# Generate the messy mock transactional data
python src/extract.py

# Run clean-up transformations and calculate key metrics
python src/transform.py

# Execute the metric monitoring & alerting system
python src/alert.py

### 3. Launch the BI Dashboard
PowerShell
streamlit run src/dashboard.py
### 4. Execute Automated Test Suites
PowerShell
$env:PYTHONPATH="." ; pytest

---

### Step 2: Push the Update to GitHub

Go down to your VS Code terminal (ensure your environment is active and you've stopped any running scripts with `Ctrl + C`), and run these three commands to push your new documentation live:

```powershell
git add README.md
git commit -m "Docs: Added comprehensive production-ready README"
git push origin main
