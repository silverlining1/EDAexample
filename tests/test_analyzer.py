"""Tests for the analysis module."""

import pandas as pd
import pytest
from eda.analyzer import analyze_data


@pytest.fixture
def clean_df():
    return pd.DataFrame({
        "Video asset ID": ["vid_001", "vid_002", "vid_003"],
        "Page name": ["Page A", "Page B", "Page A"],
        "Publish time": pd.to_datetime(["2024-01-01", "2024-01-02", "2024-01-03"]),
        "Duration (sec)": [120.0, 90.0, 150.0],
    })


def test_analyze_returns_dict(clean_df):
    """analyze_data returns a dictionary."""
    result = analyze_data(clean_df)
    assert isinstance(result, dict)


def test_analyze_total_rows(clean_df):
    """analyze_data correctly counts total rows."""
    result = analyze_data(clean_df)
    assert result["total_rows"] == 3


def test_analyze_includes_date_range(clean_df):
    """analyze_data includes date_min and date_max when date column is present."""
    result = analyze_data(clean_df)
    assert "date_min" in result
    assert "date_max" in result
    assert result["date_min"] == "2024-01-01"
    assert result["date_max"] == "2024-01-03"


def test_analyze_avg_duration(clean_df):
    """analyze_data computes average duration correctly."""
    result = analyze_data(clean_df)
    assert result["avg_duration"] == 120.0


def test_analyze_top_pages(clean_df):
    """analyze_data includes top page counts."""
    result = analyze_data(clean_df)
    assert "top_pages" in result
    assert result["top_pages"]["Page A"] == 2
