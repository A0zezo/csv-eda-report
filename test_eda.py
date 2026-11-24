import pandas as pd
from eda import report


def test_report_sections():
    df = pd.DataFrame({"a": [1, 2, 3, 4], "b": [2, 4, 6, 8], "c": ["x", "x", "y", None]})
    r = report(df)
    assert "Rows: 4" in r and "## Numeric summary" in r
    assert "a vs b: 1.000" in r
    assert "- x: 2" in r


def test_duplicates_counted():
    assert "Duplicate rows: 1" in report(pd.DataFrame({"a": [1, 1], "b": [2, 2]}))
