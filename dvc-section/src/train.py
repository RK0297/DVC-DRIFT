import pandas as pd
import yaml
import os
import pickle

# load params
with open("params.yaml") as f:
    params = yaml.safe_load(f)

lr = params["train"]["lr"]

# load processed data
df = pd.read_csv("data/processed/processed.csv")

# fake "model" (keep it simple)
model = {
    "coef": df["y"].mean(),
    "lr": lr
}

# save model
os.makedirs("models", exist_ok=True)
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)