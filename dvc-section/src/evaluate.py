import pickle
import json

# load model
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

# fake evaluation metric (deterministic)
metrics = {
    "model_coef": model["coef"],
    "learning_rate": model["lr"]
}

# write evaluation metrics
with open("eval_metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)
