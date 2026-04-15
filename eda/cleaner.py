"""Data cleaning: type coercion, deduplication, and null handling."""

import logging
import pandas as pd
import config

logger = logging.getLogger(__name__)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and prepare a raw DataFrame for analysis.

    Steps:
        1. Convert date column to datetime
        2. Convert duration column to numeric
        3. Drop rows missing critical fields
        4. Remove duplicates on ID column if present
        5. Strip whitespace from string columns

    Args:
        df: Raw DataFrame from loader.

    Returns:
        Cleaned DataFrame.
    """
    initial_rows = len(df)
    logger.info(f"Starting cleaning — {initial_rows:,} rows")

    # Strip whitespace from all string columns
    str_cols = df.select_dtypes(include=["object", "str"]).columns
    df[str_cols] = df[str_cols].apply(lambda col: col.str.strip())

    # Convert date column
    if config.DATE_COLUMN in df.columns:
        df[config.DATE_COLUMN] = pd.to_datetime(df[config.DATE_COLUMN], errors="coerce")
        invalid_dates = df[config.DATE_COLUMN].isna().sum()
        if invalid_dates:
            logger.warning(f"{invalid_dates} rows had unparseable dates — set to NaT")

    # Convert duration column
    if config.DURATION_COLUMN in df.columns:
        df[config.DURATION_COLUMN] = pd.to_numeric(df[config.DURATION_COLUMN], errors="coerce")

    # Drop rows missing critical columns that exist in this dataset
    critical = [c for c in [config.ID_COLUMN, config.DATE_COLUMN, config.PAGE_COLUMN] if c in df.columns]
    before = len(df)
    df = df.dropna(subset=critical)
    dropped = before - len(df)
    if dropped:
        logger.info(f"Dropped {dropped:,} rows with missing critical values")

    # Remove duplicates
    if config.ID_COLUMN in df.columns:
        before = len(df)
        df = df.drop_duplicates(subset=[config.ID_COLUMN])
        dupes = before - len(df)
        if dupes:
            logger.info(f"Removed {dupes:,} duplicate rows on '{config.ID_COLUMN}'")

    df = df.reset_index(drop=True)
    logger.info(f"Cleaning complete — {len(df):,} rows remaining (removed {initial_rows - len(df):,})")
    return df
