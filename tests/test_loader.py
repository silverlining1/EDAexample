"""Tests for the data loader module."""

import os
import tempfile
import pandas as pd
import pytest
from eda.loader import load_data


def test_load_valid_csv(tmp_path):
    """load_data returns a DataFrame for a valid CSV."""
    csv = tmp_path / "test.csv"
    csv.write_text("a,b,c\n1,2,3\n4,5,6\n")
    df = load_data(str(csv))
    assert df is not None
    assert len(df) == 2
    assert list(df.columns) == ["a", "b", "c"]


def test_load_missing_file():
    """load_data returns None when file does not exist."""
    result = load_data("nonexistent_file.csv")
    assert result is None


def test_load_empty_file(tmp_path):
    """load_data returns None for an empty file."""
    empty = tmp_path / "empty.csv"
    empty.write_text("")
    result = load_data(str(empty))
    assert result is None


def test_load_sample_dataset():
    """load_data successfully loads the included sample dataset."""
    sample_path = os.path.join(os.path.dirname(__file__), "..", "data", "sample_facebook.csv")
    df = load_data(sample_path)
    assert df is not None
    assert len(df) > 0
    assert "Video asset ID" in df.columns
