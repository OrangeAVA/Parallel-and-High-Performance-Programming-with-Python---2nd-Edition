"""
Generate a synthetic prices CSV similar to Kaggle's 'prices.csv'.

Usage:
  python generate_prices_sample.py --rows 200000 --out data/prices_sample.csv
"""
import argparse
import numpy as np
import pandas as pd

def main(rows:int, out:str):
    rng = np.random.default_rng(42)
    symbols = ["AAPL","MSFT","AMZN","GOOGL","META","NVDA","TSLA","JPM","UNH","V"]
    n_per_symbol = rows // len(symbols)
    dates = pd.date_range("2013-01-01", periods=n_per_symbol, freq="D")

    records = []
    for sym in symbols:
        base = np.cumsum(rng.normal(0, 1, len(dates))) + 100 + rng.random()
        open_ = base + rng.normal(0, 0.5, len(dates))
        high = open_ + np.abs(rng.normal(0, 1.2, len(dates)))
        low  = open_ - np.abs(rng.normal(0, 1.2, len(dates)))
        close = low + (high - low) * rng.random(len(dates))
        volume = np.exp(rng.normal(12, 0.6, len(dates)))  # lognormal
        adjusted = close * (1 + rng.normal(0, 0.0005, len(dates)))
        for i, d in enumerate(dates):
            records.append((sym, d.strftime("%Y-%m-%d"), float(open_[i]), float(high[i]), float(low[i]), float(close[i]), float(volume[i]), float(adjusted[i])))

    df = pd.DataFrame(records, columns=["symbol","date","open","high","low","close","volume","adjusted"])
    df.insert(0, "Unnamed: 0", range(len(df)))  # mimic typical CSV exports
    df.to_csv(out, index=False)
    print(f"Wrote {len(df):,} rows to {out}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--rows", type=int, default=200_000)
    ap.add_argument("--out", type=str, default="data/prices_sample.csv")
    args = ap.parse_args()
    main(args.rows, args.out)
