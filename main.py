"""CLI entrypoint for the EDA Toolkit.

Usage:
    python main.py
    python main.py --file path/to/data.csv
    python main.py --file path/to/data.csv --output results/
"""

import argparse
import logging
import os
import sys

import config
from eda.loader import load_data
from eda.cleaner import clean_data
from eda.analyzer import analyze_data
from eda.visualizer import visualize_data
from eda.reporter import write_report

logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("eda.main")


def parse_args():
    parser = argparse.ArgumentParser(description="EDA Toolkit — Code Alchemist Labs")
    parser.add_argument("--file", default=config.DATA_FILE, help="Path to input CSV file")
    parser.add_argument("--output", default=config.OUTPUT_DIR, help="Directory for output files")
    return parser.parse_args()


def main():
    args = parse_args()
    os.makedirs(args.output, exist_ok=True)

    logger.info("Starting EDA pipeline")
    logger.info(f"Input file: {args.file}")
    logger.info(f"Output directory: {args.output}")

    # Step 1: Load
    df = load_data(args.file)
    if df is None:
        logger.error("Failed to load data. Exiting.")
        sys.exit(1)

    # Step 2: Clean
    df = clean_data(df)
    if df.empty:
        logger.error("No data remaining after cleaning. Exiting.")
        sys.exit(1)

    # Step 3: Analyze
    results = analyze_data(df)

    # Step 4: Visualize
    chart_paths = visualize_data(df, results, args.output)

    # Step 5: Report
    report_path = write_report(args.file, df, results, chart_paths, args.output)

    logger.info(f"EDA complete. Report saved to: {report_path}")
    print(f"\n✅ Done! Report → {report_path}")


if __name__ == "__main__":
    main()
