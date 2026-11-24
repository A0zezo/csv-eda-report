"""Generate a Markdown EDA report for any CSV file using pandas."""
import sys
import pandas as pd


def report(df):
    out = [f"# EDA report", "", f"Rows: {len(df)}  Columns: {df.shape[1]}", ""]
    out += ["## Columns", "", "| column | dtype | missing | unique |", "|---|---|---|---|"]
    for c in df.columns:
        out.append(f"| {c} | {df[c].dtype} | {int(df[c].isna().sum())} | {df[c].nunique()} |")
    num = df.select_dtypes("number")
    if not num.empty:
        out += ["", "## Numeric summary", "", num.describe().T.round(3).to_markdown()]
    if num.shape[1] > 1:
        corr = num.corr().abs().where(lambda m: ~(m.index.values[:, None] == m.columns.values[None, :]))
        pairs = corr.stack().sort_values(ascending=False)
        pairs = pairs[[a < b for a, b in pairs.index]].head(3)
        out += ["", "## Strongest absolute correlations", ""]
        out += [f"- {a} vs {b}: {v:.3f}" for (a, b), v in pairs.items()]
    cat = df.select_dtypes(exclude="number")
    for c in cat.columns:
        out += ["", f"## Top values: {c}", ""]
        out += [f"- {k}: {v}" for k, v in df[c].value_counts().head(5).items()]
    dup = int(df.duplicated().sum())
    out += ["", f"Duplicate rows: {dup}"]
    return "\n".join(out)


if __name__ == "__main__":
    print(report(pd.read_csv(sys.argv[1])))
