# DVC Pipeline Demo

A simple ML pipeline using Data Version Control (DVC).

## Pipeline Stages

```
data/raw → prepare.py → data/processed → train.py → models/model.pkl → evaluate.py → metrics
```

## Quick Start

```bash
# Run full pipeline
dvc repro

# View metrics
dvc metrics show

# Compare experiments
dvc params diff
```

## Files

| File | Purpose |
|------|---------|
| `dvc.yaml` | Pipeline definition |
| `params.yaml` | Tunable parameters |
| `src/prepare.py` | Data preprocessing |
| `src/train.py` | Model training |
| `src/evaluate.py` | Model evaluation |

## Parameters

```yaml
prepare:
  multiplier: 5
train:
  lr: 0.2
```
