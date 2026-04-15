"""Tests for the data cleaning module."""

import pandas as pd
import pytest
from unittest.mock import patch
from eda.cleaner import clean_data


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "Video asset ID": ["vid_001", "vid_002", "vid_003", "vid_002"],
        "Page name": ["  Page A  ", "Page B", "Page C", "Page B"],
        "Publish time": ["2024-01-01", "2024-01-02", "bad-date", "2024-01-02"],
        "Duration (sec)": [120, 90, "not-a-number", 90],
    })


def test_strips_whitespace(sample_df):
    """clean_data strips leading/trailing whitespace from string columns."""
    cleaned = clean_data(sample_df.copy())
    assert not any(cleaned["Page name"].str.startswith(" "))
    assert not any(cleaned["Page name"].str.endswith(" "))


def test_deduplicates_on_id(sample_df):
    """clean_data removes duplicate rows based on ID column."""
    cleaned = clean_data(sample_df.copy())
    assert cleaned["Video asset ID"].nunique() == cleaned["Video asset ID"].count()


def test_coerces_duration_to_numeric(sample_df):
    """clean_data converts Duration column to numeric, coercing bad values to NaN."""
    cleaned = clean_data(sample_df.copy())
    assert pd.api.types.is_numeric_dtype(cleaned["Duration (sec)"])


def test_returns_dataframe(sample_df):
    """clean_data always returns a DataFrame."""
    result = clean_data(sample_df.copy())
    assert isinstance(result, pd.DataFrame)


def test_empty_dataframe_input():
    """clean_data handles an empty DataFrame without crashing."""
    result = clean_data(pd.DataFrame())
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 0
