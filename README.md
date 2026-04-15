# EDA Toolkit — Social & Business Data Analysis

> A production-grade Exploratory Data Analysis (EDA) toolkit built for cleaning, analyzing, and visualizing structured business datasets. Built by [Code Alchemist Labs](https://codealchemistlabs.com).

---

## What This Does

This toolkit takes raw CSV data (social media exports, CRM data, sales reports, etc.), cleans it, runs statistical analysis, and generates publication-ready charts and a summary report — automatically.

**Real-world use cases:**
- Analyze Facebook/Instagram content performance data
- Explore CRM or lead data before building a model
- Generate a data quality report for a client dataset
- Rapid EDA before any ML or automation pipeline

---

## Project Structure

```
EDAexample/
├── eda/
│   ├── __init__.py
│   ├── loader.py          # Data loading with validation
│   ├── cleaner.py         # Data cleaning and type coercion
│   ├── analyzer.py        # Statistical analysis
│   ├── visualizer.py      # Chart generation (matplotlib/seaborn)
│   └── reporter.py        # Markdown summary report writer
├── data/
│   └── sample_facebook.csv  # Sample dataset for demo
├── outputs/               # Generated charts and reports (git-ignored)
├── main.py                # CLI entrypoint
├── config.py              # Config via environment variables
├── requirements.txt
├── .env.example
└── README.md
```

---

## Quickstart

```bash
# 1. Clone and install
git clone https://github.com/silverlining1/EDAexample.git
cd EDAexample
pip install -r requirements.txt

# 2. Copy and configure environment
cp .env.example .env

# 3. Run against a dataset
python main.py --file data/sample_facebook.csv

# 4. Check outputs/
# → outputs/report.md
# → outputs/videos_per_day.png
# → outputs/duration_distribution.png
# → outputs/top_pages.png
```

---

## Configuration

Copy `.env.example` to `.env` and set values:

```env
DATA_FILE=data/sample_facebook.csv
OUTPUT_DIR=outputs
LOG_LEVEL=INFO
DATE_COLUMN=Publish time
ID_COLUMN=Video asset ID
```

---

## Output Example

After running, `outputs/report.md` will contain:

```
# EDA Report — facebook_data.csv
Generated: 2026-04-15 00:11:00

## Dataset Overview
- Total rows: 1,204
- Columns: 12
- Missing values: 3 (0.25%)

## Key Metrics
- Average video duration: 142.3 seconds
- Date range: 2023-01-01 → 2024-06-30
- Top page: "Brand XYZ" (204 videos)

## Charts Generated
- videos_per_day.png
- duration_distribution.png
- top_pages.png
```

---

## Tech Stack

- **Python 3.10+**
- **pandas** — data loading, cleaning, transformation
- **matplotlib / seaborn** — visualization
- **python-dotenv** — config management
- **logging** — structured runtime logs

---

## Part of the Code Alchemist Labs Python Portfolio

This project is part of a 4-project Python portfolio series:

| # | Project | Focus |
|---|---|---|
| 1 | **EDA Toolkit** (this) | Data cleaning + analysis |
| 2 | [ML Pipeline](https://github.com/silverlining1/ml-pipeline) | scikit-learn model training + evaluation |
| 3 | [Automated Data Pipeline](https://github.com/silverlining1/automated-data-pipeline) | API ingestion + reporting |
| 4 | [Prediction API](https://github.com/silverlining1/prediction-api) | FastAPI ML serving |

---

*Built by Earnest M. Walker · [Code Alchemist Labs](https://codealchemistlabs.com)*
