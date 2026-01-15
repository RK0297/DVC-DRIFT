import pandas as pd
import yaml
import os
import json

# load parameters
with open("params.yaml") as f:
    params = yaml.safe_load(f)

m = params["prepare"]["multiplier"]

# load data
df = pd.read_csv("data/raw/data.csv", header=None)
df.columns = ["x", "y"]

# apply parameter
df["y"] = df["y"] * m

# save processed data
os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/processed.csv", index=False)

# write metrics
metrics = {
    "rows": len(df),
    "multiplier": m
}

with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)
