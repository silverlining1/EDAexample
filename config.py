"""Central configuration loaded from environment variables."""

import os
from dotenv import load_dotenv

load_dotenv()

DATA_FILE = os.getenv("DATA_FILE", "data/sample_facebook.csv")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "outputs")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
DATE_COLUMN = os.getenv("DATE_COLUMN", "Publish time")
ID_COLUMN = os.getenv("ID_COLUMN", "Video asset ID")
DURATION_COLUMN = os.getenv("DURATION_COLUMN", "Duration (sec)")
PAGE_COLUMN = os.getenv("PAGE_COLUMN", "Page name")
TOP_N_PAGES = int(os.getenv("TOP_N_PAGES", "10"))
