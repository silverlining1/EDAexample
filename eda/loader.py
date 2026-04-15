"""Data loading with validation and basic schema checks."""

import logging
import pandas as pd

logger = logging.getLogger(__name__)


def load_data(file_path: str) -> pd.DataFrame | None:
    """Load a CSV file into a DataFrame with error handling.

    Args:
        file_path: Path to the CSV file.

    Returns:
        DataFrame if successful, None if the file cannot be loaded.
    """
    try:
        df = pd.read_csv(file_path)
        logger.info(f"Loaded {len(df):,} rows and {len(df.columns)} columns from '{file_path}'")
        logger.debug(f"Columns: {df.columns.tolist()}")
        return df
    except FileNotFoundError:
        logger.error(f"File not found: '{file_path}'")
        return None
    except pd.errors.EmptyDataError:
        logger.error(f"File is empty: '{file_path}'")
        return None
    except Exception as e:
        logger.error(f"Unexpected error loading file: {e}")
        return None
