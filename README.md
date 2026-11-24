# csv-eda-report

One-file pandas script that turns any CSV into a Markdown EDA report: column types, missing values, unique counts, numeric summary, top absolute correlations, top categorical values and duplicate count.

`sample.csv` is synthetic (200 random rows generated with NumPy, 10 weights blanked out).

## Run

```bash
pip install -r requirements.txt
python eda.py sample.csv > report.md
pytest
```

## Output (reproduced)

````
# EDA report

Rows: 200  Columns: 4

## Columns

| column | dtype | missing | unique |
|---|---|---|---|
| height_cm | float64 | 0 | 154 |
| weight_kg | float64 | 10 | 129 |
| city | object | 0 | 3 |
| age | int64 | 0 | 47 |

## Numeric summary

|           |   count |    mean |    std |   min |     25% |    50% |     75% |   max |
|:----------|--------:|--------:|-------:|------:|--------:|-------:|--------:|------:|
| height_cm |     200 | 169.264 |  9.268 | 142.9 | 163.425 | 170.05 | 175.5   | 198.7 |
| weight_kg |     190 |  64.362 |  6.654 |  48.1 |  60.525 |  64.75 |  68.175 |  84.3 |
| age       |     200 |  42.385 | 14.022 |  18   |  30     |  42.5  |  56     |  64   |

## Strongest absolute correlations

- height_cm vs weight_kg: 0.734
- age vs height_cm: 0.077
- age vs weight_kg: 0.017

## Top values: city

- Cairo: 102
- Alexandria: 57
- Giza: 41

Duplicate rows: 0
````

```
$ pytest -q
2 passed in 0.18s
```
