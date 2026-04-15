"""Statistical analysis of cleaned DataFrame."""

import logging
import pandas as pd
import config

logger = logging.getLogger(__name__)


def analyze_data(df: pd.DataFrame) -> dict:
    """Run statistical analysis and return results as a dictionary.

    Args:
        df: Cleaned DataFrame.

    Returns:
        Dictionary of analysis results.
    """
    results = {}
    logger.info("Running analysis")

    results["total_rows"] = len(df)
    results["total_columns"] = len(df.columns)
    results["missing_values"] = int(df.isna().sum().sum())
    results["missing_pct"] = round(results["missing_values"] / (len(df) * len(df.columns)) * 100, 2)
    results["column_names"] = df.columns.tolist()

    # Date range
    if config.DATE_COLUMN in df.columns:
        results["date_min"] = str(df[config.DATE_COLUMN].min().date())
        results["date_max"] = str(df[config.DATE_COLUMN].max().date())
        results["videos_per_day"] = df.groupby(df[config.DATE_COLUMN].dt.date).size()

    # Duration stats
    if config.DURATION_COLUMN in df.columns:
        results["avg_duration"] = round(df[config.DURATION_COLUMN].mean(), 2)
        results["duration_stats"] = df[config.DURATION_COLUMN].describe().to_dict()

    # Top pages
    if config.PAGE_COLUMN in df.columns:
        results["top_pages"] = df[config.PAGE_COLUMN].value_counts().head(config.TOP_N_PAGES)

    logger.info(f"Analysis complete — {results['total_rows']:,} rows analyzed")
    return results
